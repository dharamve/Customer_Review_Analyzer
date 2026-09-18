# 📊 Customer Review Sentiment & Complaint Analyzer

An NLP and Machine Learning project that analyzes e-commerce customer reviews, predicts sentiment, identifies common complaint areas, and presents business insights through an interactive dashboard.

## 🚀 Project Overview

Customer reviews contain valuable information about product quality, delivery, pricing, packaging, and customer service.

This project uses Natural Language Processing (NLP) and Machine Learning to automatically analyze customer feedback and classify reviews into:

* Positive
* Neutral
* Negative

The project also identifies common complaint categories in negative reviews.

## 🎯 Objectives

* Clean and preprocess customer review text
* Perform exploratory data analysis
* Apply NLP techniques to customer reviews
* Convert text into numerical features using TF-IDF
* Train multiple machine learning models
* Compare model performance
* Predict sentiment for new reviews
* Identify common customer complaint categories
* Build a Power BI dashboard
* Deploy an interactive Streamlit application

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* Matplotlib
* Seaborn
* WordCloud
* Joblib
* Streamlit
* Power BI

## 🧠 NLP Techniques

The project uses:

1. Text normalization
2. Stopword removal
3. Tokenization
4. TF-IDF Vectorization
5. Unigram and bigram features
6. Text classification

## 🤖 Machine Learning Models

The following models are compared:

* Multinomial Naive Bayes
* Logistic Regression
* Linear Support Vector Machine

Model performance is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

## 📊 Business Analysis

Negative reviews are further categorized into topics such as:

* Delivery
* Product Quality
* Battery
* Customer Support
* Packaging
* Price
* Other

This helps identify the areas responsible for customer dissatisfaction.

## 📈 Power BI Dashboard

The dashboard contains:

* Total Reviews
* Average Rating
* Positive Reviews
* Negative Reviews
* Sentiment Distribution
* Rating vs Sentiment
* Major Complaint Categories
* Product-wise Sentiment Analysis

Interactive filters are provided for product, rating, sentiment, price, and complaint category.

## 🌐 Streamlit Application

The Streamlit application allows users to enter a customer review and receive a predicted sentiment.

Example:

> "The product is excellent and delivery was very fast."

Prediction:

**Positive**

## 📂 Project Structure

```text
NLP_Customer_Review_Analyzer/
│
├── data/
├── notebooks/
├── models/
├── outputs/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project

```bash
cd NLP_Customer_Review_Analyzer
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model

Open:

```text
notebooks/NLP_Sentiment_Analysis.ipynb
```

Run all cells.

### 5. Run the application

```bash
streamlit run app.py
```

## 📌 Dataset

The project uses the Flipkart Product Reviews with Sentiment dataset.

Dataset source:

https://www.kaggle.com/dsv/4940809

## 📌 Future Improvements

* Implement transformer-based models such as BERT
* Perform aspect-based sentiment analysis
* Add multilingual sentiment analysis
* Add real-time review monitoring
* Improve complaint classification
* Deploy the application to a cloud platform

## 👨‍💻 Author

Dharamveer Prakash P

Data Analytics / Machine Learning Enthusiast
