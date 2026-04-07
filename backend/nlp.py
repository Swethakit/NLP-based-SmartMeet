from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt",   # 👈 FORCE PyTorch (IMPORTANT)
    device=-1
)

def analyze_sentiment(text):

    result = sentiment_model(text)[0]

    return {
        "label": result["label"],
        "score": round(result["score"], 3)
    }