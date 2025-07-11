from transformers import MarianMTModel, MarianTokenizer

# Desteklenen diller ve Helsinki-NLP model kodları
LANG_MODEL_MAP = {
    "turkish": "tr",
    "english": "en",   # İngilizce için çeviri genelde gerekmez, direk döndürülür
    "german": "de",
    "french": "fr",
    "spanish": "es",
    "italian": "it",
    "russian": "ru",
}

class Translator:
    def __init__(self, source_lang: str):
        self.source_lang = source_lang.lower()
        self.tokenizer = None
        self.model = None
        
        if self.source_lang == "english":
            # İngilizce ise çeviri yapma, direkt döndür
            self.translate = self._identity
        else:
            lang_code = LANG_MODEL_MAP.get(self.source_lang)
            if not lang_code:
                raise ValueError(f"Desteklenmeyen dil: {source_lang}")
            model_name = f"Helsinki-NLP/opus-mt-{lang_code}-en"
            self.tokenizer = MarianTokenizer.from_pretrained(model_name)
            self.model = MarianMTModel.from_pretrained(model_name)

    def _identity(self, text: str) -> str:
        return text

    def translate(self, text: str) -> str:
        # Bu metot init sırasında override edilir
        pass

    def translate_batch(self, texts: list[str]) -> list[str]:
        """Birden fazla metni çevir"""
        if self.source_lang == "english":
            return texts
        inputs = self.tokenizer(texts, return_tensors="pt", padding=True)
        translated = self.model.generate(**inputs)
        return [self.tokenizer.decode(t, skip_special_tokens=True) for t in translated]
