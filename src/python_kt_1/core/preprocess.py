def _load_stopwords() -> set:
    f = open("./stopwords.txt", encoding="utf-8")
    stopwords = f.read().splitlines()
    f.close() 
    return set(stopwords)

def filter_stopwords(words: list[str]) -> list[str]:
    stopwords = _load_stopwords()
    print(stopwords)
    return words