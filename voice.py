from gtts import gTTS
from collections import Counter
import os
import uuid

def generate_voice_summary(words, artist_name, top_n=10, language='tr') -> str:
    """
    En sık geçen kelimeleri alır, Türkçe sesli özet üretir ve mp3 olarak kaydeder.

    Args:
        words (List[str]): İşlenmiş kelime listesi
        artist_name (str): Sanatçı adı
        top_n (int): En sık geçen kaç kelimeye göre seslendirilsin
        language (str): gTTS dili ('tr' için Türkçe)

    Returns:
        str: Kaydedilen mp3 dosyasının yolu
    """
    word_counts = Counter(words)
    most_common = word_counts.most_common(top_n)

    if not most_common:
        raise ValueError("Sesli özet için yeterli kelime bulunamadı.")

    # Konuşma metni hazırla
    text = f"{artist_name} şarkılarında en çok tekrar eden {top_n} kelime şunlardır: "
    text += ", ".join([f"{kelime} ({adet} kez)" for kelime, adet in most_common]) + "."

    # Ses dosyasını oluştur
    tts = gTTS(text=text, lang=language, slow=False)
    filename = f"{uuid.uuid4().hex}.mp3"
    voice_path = os.path.join("static", "plots", filename)
    os.makedirs(os.path.dirname(voice_path), exist_ok=True)
    tts.save(voice_path)

    return voice_path
