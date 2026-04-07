from keybert import KeyBERT

kw_model = KeyBERT()

def detect_topics(text):

    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1,2),
        stop_words="english",
        top_n=5
    )

    topics = [k[0] for k in keywords]

    return topics