from ..core.preprocess import filter_stopwords

def top_words(
    text: str, 
    normalize_mode: Literal["stemming", "lemmatization"] = "stemming", 
    pos: list[str] = ["__all__"]
):
    """Подсчет топ-N-важных слов.

    Получает текст, разбивает на слова, убирает пунктуацию и пробельные символы,
    фильтрует стоп-слова, нормализует (либо стемминг, либо лемматизация),
    подсчитывает и возвращает список кортежей для топ-N-важных слов.
    """
    
    return
    