import streamlit as st
import joblib
import re

from nltk.corpus import stopwords

st.set_page_config(
page_title="Customer Sentiment Analyzer",
page_icon="📊",
layout="centered"
)

# Load model

model = joblib.load(
"models/sentiment_model.pkl"
)

vectorizer = joblib.load(
"models/tfidf_vectorizer.pkl"
)

stop_words = set(
stopwords.words("english")
)

def clean_text(text):

```
text = text.lower()

text = re.sub(
    r"http\S+|www\S+",
    "",
    text
)

text = re.sub(
    r"[^a-zA-Z\s]",
    "",
    text
)

words = text.split()

words = [
    word
    for word in words
    if word not in stop_words
]

return " ".join(words)
```

st.title("📊 Customer Review Sentiment Analyzer")

st.write(
"Enter a customer review and the NLP model "
"will predict its sentiment."
)

review = st.text_area(
"Enter customer review:"
)

if st.button("Analyze Sentiment"):

```
if review.strip() == "":
    st.warning(
        "Please enter a review."
    )

else:

    cleaned = clean_text(review)

    transformed = vectorizer.transform(
        [cleaned]
    )

    prediction = model.predict(
        transformed
    )[0]

    if prediction == "positive":

        st.success(
            "😊 Positive Sentiment"
        )

    elif prediction == "negative":

        st.error(
            "😡 Negative Sentiment"
        )

    else:

        st.info(
            "😐 Neutral Sentiment"
        )
```
