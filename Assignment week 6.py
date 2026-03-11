from transformers import pipeline
sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",

)

text = "The new AI product significantly improved our company productivity."

result = sentiment(text)

print("\nSentiment Analysis Result:")
print(result)