Lyrics Insight

Proje Amacı
Bu proje, müzik sanatçılarının şarkı sözlerinin içeriklerini metinsel olarak analiz etmek, öne çıkan kelimeleri görselleştirmek ve kullanıcıya sesli özet sunmak amacıyla geliştirilmiştir. Doğal dil işleme (NLP), veri görselleştirme ve metinden konuşma teknolojileri bir araya getirilerek, kullanıcıya hem etkileşimli hem de öğretici bir deneyim sunar.

🧠 Temel Özellikler
🎵 Genius API üzerinden sanatçının şarkı sözleri alınır.

🧹 Alınan şarkı sözleri temizlenir, stopword (önemsiz kelime) filtresi uygulanır.

📊 En sık geçen kelimeler matplotlib ile görselleştirilir.

🔊 gTTS ile sesli özet üretilir.

🗣️ Kullanıcı, belirli bir kelimenin kaç defa geçtiğini sorgulayabilir.

🌍 Çeşitli dillerde (TR, EN, DE, FR) analiz yapılabilir.

🛠️ Kullanılan Teknolojiler ve Kütüphaneler
Teknoloji/Kütüphane	Açıklama
Flask	Web uygulamasının temel framework’ü
Genius API (lyricsgenius)	Şarkı sözlerinin elde edilmesi
NLTK	Doğal dil işleme ve stopwords filtreleme
matplotlib	Kelime frekans grafiği çizimi
gTTS	Metni ses dosyasına dönüştürme
tqdm	Şarkı yükleme sırasında ilerleme çubuğu
HTML/CSS	Kullanıcı arayüzü tasarımı
Bootstrap & Google Fonts	Arayüz estetiğini artırma

📁 Dosya Yapısı
bash
Copy
Edit
lyrics_insight/
│
├── app.py                     # Ana Flask uygulama dosyası
├── genius.py                 # Genius API üzerinden söz alma işlemleri
├── nlp.py                    # Helsinki NLP ile çoklu dil desteği (çevrim)
├── analysis.py               # Kelime analizi ve grafik üretimi
├── voice.py                  # Sesli özet üretimi (gTTS)
├── static/
│   ├── css/style.css         # Arayüz stili
│   └── plots/                # Grafik ve ses dosyalarının çıktısı
├── templates/
│   ├── index.html            # Ana form sayfası
│   └── result.html           # Analiz sonuçlarının gösterildiği sayfa
├── requirements.txt          # Kurulması gereken tüm Python paketleri
└── README.md                 # Proje açıklaması (bu dosya)
🔧 Kurulum Adımları
1. Depoyu Klonlayın

git clone https://github.com/kullaniciadi/lyrics-insight.git
cd lyrics-insight

2. Sanal Ortam Oluşturun ve Aktif Edin

python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

3. Gereksinimleri Kurun

pip install -r requirements.txt

4. Gerekli NLTK Verilerini İndirin

import nltk
nltk.download('stopwords')

🔑 Genius API Token Nasıl Alınır?
https://genius.com/api-clients adresine gidin.

Hesabınızla giriş yaptıktan sonra bir “API Client” oluşturun.

“Client Access Token” kısmında göreceğiniz token'ı alın.

Bu token'ı formda ilgili alana yapıştırarak analiz başlatabilirsiniz.

🔄 Desteklenen Diller
Dil	Kod
Türkçe	tr
İngilizce	en
Almanca	de
Fransızca	fr

🧪 Örnek Kullanım Senaryosu
Kullanıcı, analiz etmek istediği sanatçının adını ve Genius API Token'ını girer.

Sistem, sanatçının popüler 50 şarkısının sözlerini indirir.

Metin temizlenir, analiz edilir ve kelime frekansı hesaplanır.

En sık geçen kelimelerden grafik oluşturulur.

Top 10 kelimenin sesi otomatik olarak üretilir.

Kullanıcı dilerse belirli bir kelimenin kaç defa geçtiğini sorgulayabilir.

📚 Akademik Katkılar
Doğal dil işleme ile metin temizleme ve anlam çıkarımı

Veri görselleştirme ile metinsel veriden içgörü üretme

Sesli özetleme ile erişilebilirlik ve kullanıcı etkileşimini artırma

Çok dilli analiz desteği ile küresel kullanılabilirlik sağlama

📌 Notlar
Bu uygulama sadece eğitim ve araştırma amaçlı geliştirilmiştir.

Gerçek zamanlı ve ticari kullanım için daha gelişmiş hata kontrolü, güvenlik ve veritabanı entegrasyonu gereklidir.

🧑‍💻 Geliştirici
Mahmut Sibal
@byteByteÖğren
📍 Türkiye