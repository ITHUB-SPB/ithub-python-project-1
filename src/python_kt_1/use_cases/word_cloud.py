from typing import Literal
from wordcloud import WordCloud
from pathlib import Path
from time import strftime, localtime
import re

# Импорты для предобработки
try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import SnowballStemmer
    from nltk.stem import WordNetLemmatizer

    # Загрузка ресурсов NLTK
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)

    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)

    NLTK_AVAILABLE = True
except ImportError:
    NLTK_AVAILABLE = False
    print("Предупреждение: NLTK не установлен. Стемминг и лемматизация будут недоступны.")
from ..core.preprocess import filter_stopwords

def word_cloud(
    text: str, 
    preprocess_mode: Literal["basic", "stemming", "lemmatization"] = "stemming" 
):
    """Построение облака важных слов.

    Получает текст, выполняет базовую предобработку (разбивает на слова, 
    убирает пунктуацию и пробельные символы, фильтрует стоп-слова. 

    При указании режима предобработки, отличного от базового, нормализует 
    (стеммингом либо лемматизацией). 

    Возможности:
    - сохранение результата (изображения) в файл
    - три уровня предобработки (базовый, стемминг, лемматизация).
    """

    # Генерируем имя файла
    timestamp = strftime("%H_%M_%S", localtime())
    output_file = Path(f"{timestamp}_wordcloud.png")

    # Предобрабатываем текст в зависимости от режима
    if preprocess_mode == "basic":
        # Для basic используем текст без предобработки
        processed_text = text
        word_count = len(text.split())
        unique_count = len(set(text.lower().split()))
    else:
        # Для stemming и lemmatization применяем полную предобработку
        processed_text = preprocess_text(text, preprocess_mode)
        words = processed_text.split()
        word_count = len(words)
        unique_count = len(set(words))

    # Создаем облако слов
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        max_words=200,
        contour_width=1,
        contour_color='steelblue',
        random_state=42
    ).generate(processed_text)

    # Сохраняем в файл
    wordcloud.to_file(str(output_file))

    return f"Облако слов создано: режим '{preprocess_mode}', слов: {word_count}, уникальных: {unique_count}, файл: {output_file}"