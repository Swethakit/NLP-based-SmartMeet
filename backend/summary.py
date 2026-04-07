from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="t5-small",
    framework="pt"
)

def summarize(text):
    # 🛡️ Safety: avoid empty text crash
    if not text or len(text.strip()) == 0:
        return "No content to summarize."

    # 🛡️ Shorten very long text (model limit)
    text = text[:1000]

    result = summarizer(
        text,
        max_length=120,
        min_length=20,
        do_sample=False
    )

    # ✅ FIXED LINE
    return result[0]["summary_text"]