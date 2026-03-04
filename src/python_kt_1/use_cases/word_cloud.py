import re
from typing import Literal
from wordcloud import WordCloud
from ..core.preprocess import clean_words, filter_stopwords, stem_words, lemmatize_words

def word_cloud(
    text: str, 
    preprocess_mode: Literal["basic", "stemming", "lemmatization"] = "stemming" 
):
    raw_words = re.findall(r'\b\w+\b', text)
    cleaned = clean_words(raw_words)
    filtered = filter_stopwords(cleaned)

    if preprocess_mode == "stemming":
        final_words = stem_words(filtered)
    elif preprocess_mode == "lemmatization":
        final_words = lemmatize_words(filtered)
    else: # basic
        final_words = filtered

    ready_text = " ".join(final_words)

    if not ready_text.strip(): # удаляет пробелы в начале и конце
        ready_text = "нет данных"
        
    wc = WordCloud(width=800, height=400, background_color="white")
    return wc.generate(ready_text)
