import re
import nltk
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from typing import List
import os

# Stopwords varsa indir
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


def process_lyrics(lyrics_list: List[str], language: str = "turkish", min_song_count: int = 2) -> List[str]:
    """
    Şarkı sözlerini temizler, stopword'leri çıkarır ve kullanılabilir kelimeleri döner.
    """
    stop_words = set(stopwords.words(language.lower())) if language.lower() in stopwords.fileids() else set()
    stop_words.update(["lyrics", "oh", "yeah", "la", "im", "da", "de"])

    if language.lower() == "turkish":
        stop_words.update(["ben", "sen", "bi", "bir", "bana", "sana", "beni", "seni"])

    word_song_count = {}
    all_words = []

    for lyrics in lyrics_list:
        clean = re.sub(r"\[.*?\]", "", lyrics.lower())
        clean = re.sub(r"\(.*?\)", "", clean)
        clean = re.sub(r"[^\w\s]", "", clean)

        words = set([w for w in clean.split() if w not in stop_words and not w.isdigit()])
        for word in words:
            word_song_count[word] = word_song_count.get(word, 0) + 1

    valid_words = {w for w, c in word_song_count.items() if c >= min_song_count}

    for lyrics in lyrics_list:
        clean = re.sub(r"\[.*?\]", "", lyrics.lower())
        clean = re.sub(r"\(.*?\)", "", clean)
        clean = re.sub(r"[^\w\s]", "", clean)
        words = [w for w in clean.split() if w in valid_words]
        all_words.extend(words)

    return all_words


def generate_word_plot(words: List[str], artist_name: str, top_n: int = 20) -> str:
    """
    Kelimelerin sıklık grafiğini üretir ve static/plots/ klasörüne kaydeder.
    Dönüş: sadece dosya adı (örnek: "taylorswift_plot.png")
    """
    word_counts = Counter(words)
    most_common = word_counts.most_common(top_n)

    if not most_common:
        raise ValueError("Yeterli kelime verisi bulunamadı.")

    labels, counts = zip(*most_common)

    plt.figure(figsize=(10, 5))
    bars = plt.bar(labels, counts, color='skyblue')
    plt.xticks(rotation=45)
    plt.title(f"{artist_name} – En Sık {top_n} Kelime", fontsize=14)
    plt.xlabel("Kelime")
    plt.ylabel("Frekans")

    for bar, count in zip(bars, counts):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, str(count),
                 ha='center', va='bottom', fontsize=8)

    plt.tight_layout()

    # Dosya yolu oluştur
    filename = f"{artist_name.replace(' ', '_').lower()}_plot.png"
    save_path = os.path.join("static", "plots", filename)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()

    return filename
