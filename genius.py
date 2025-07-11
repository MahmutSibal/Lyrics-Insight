from lyricsgenius import Genius
import re
import time
from typing import List
from difflib import SequenceMatcher
from tqdm import tqdm

def _calculate_similarity(text1: str, text2: str) -> float:
    """İki metin arasındaki benzerliği hesaplar (0.0 – 1.0 arası)."""
    text1_clean = re.sub(r'[^\w\s]', '', text1.lower().strip())
    text2_clean = re.sub(r'[^\w\s]', '', text2.lower().strip())
    return SequenceMatcher(None, text1_clean, text2_clean).ratio()

def _remove_duplicates(lyrics_list: List[str], threshold: float = 0.85) -> List[str]:
    """Benzer şarkı sözlerini listeden çıkarır."""
    unique_lyrics = []
    for lyrics in lyrics_list:
        is_duplicate = False
        for existing in unique_lyrics:
            if _calculate_similarity(lyrics, existing) >= threshold:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_lyrics.append(lyrics)
    return unique_lyrics

def get_artist_lyrics(genius_token: str, artist_name: str) -> List[str]:
    """
    Genius API'den sanatçının şarkı sözlerini getirir.
    """
    print(f"🎤 '{artist_name}' için şarkı sözleri çekiliyor...")
    genius = Genius(genius_token, timeout=15, retries=3)
    
    try:
        artist = genius.search_artist(artist_name, max_songs=50, sort="popularity")
    except Exception as e:
        raise Exception(f"Genius API hatası: {str(e)}")

    if not artist or not artist.songs:
        raise Exception("Sanatçı bulunamadı ya da şarkı listesi boş.")

    lyrics_list = []
    for song in tqdm(artist.songs, desc="Şarkılar indiriliyor"):
        try:
            lyrics_list.append(song.lyrics)
        except:
            continue

    if not lyrics_list:
        raise Exception("Şarkı sözleri bulunamadı.")

    # Benzer şarkıları temizle
    unique_lyrics = _remove_duplicates(lyrics_list)
    print(f"🎶 {len(unique_lyrics)} özgün şarkı sözü bulundu.")
    return unique_lyrics
