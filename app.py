from flask import Flask, render_template, request, redirect, url_for
from genius import get_artist_lyrics
from analysis import process_lyrics, generate_word_plot
from voice import generate_voice_summary
from collections import Counter
import os

app = Flask(__name__)

# Geçici önbellek (Demo amaçlı. Gerçek sistemde session/db kullanılmalı)
cached_data = {
    "artist": None,
    "lyrics_list": None,
    "processed_words": None,
    "word_counts": None,
    "voice_file": None,
    "image_file": None
}

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        genius_token = request.form.get("genius_token")
        artist_name = request.form.get("artist_name")
        language = request.form.get("language", "turkish")

        if not genius_token or not artist_name:
            error = "Lütfen hem Genius tokenini hem sanatçı adını girin."
            return render_template("index.html", error=error)

        try:
            # Şarkı sözlerini al
            lyrics_list = get_artist_lyrics(genius_token, artist_name)

            # Kelimeleri işle
            processed_words = process_lyrics(lyrics_list, language=language)

            # Say
            word_counts = Counter(processed_words)

            # Grafik oluştur
            image_filename = generate_word_plot(processed_words, artist_name)
            image_path = os.path.join("plots", image_filename)

            # Sesli özet oluştur
            voice_path = generate_voice_summary(processed_words, artist_name, language='tr' if language == 'turkish' else 'en')

            # Verileri sakla
            cached_data.update({
                "artist": artist_name,
                "lyrics_list": lyrics_list,
                "processed_words": processed_words,
                "word_counts": word_counts,
                "voice_file": voice_path,
                "image_file": image_path
            })

            return redirect(url_for("result"))

        except Exception as e:
            error = f"Hata oluştu: {str(e)}"

    return render_template("index.html", error=error)


@app.route("/result", methods=["GET", "POST"])
def result():
    if not cached_data["processed_words"]:
        return redirect(url_for("index"))

    search_word = None
    count = None

    if request.method == "POST":
        search_word = request.form.get("search_word", "").strip().lower()
        if search_word:
            count = cached_data["word_counts"].get(search_word, 0)

    return render_template(
        "result.html",
        artist=cached_data["artist"],
        voice_file=cached_data["voice_file"],
        image_file=cached_data["image_file"],
        count=count,
        search_word=search_word
    )


if __name__ == "__main__":
    app.run(debug=True)
