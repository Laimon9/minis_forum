import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize

# Завантаження моделі SpaCy для англійської мови
nlp = spacy.load('en_core_web_sm')

# Використання VADER для аналізу настроїв
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    return sia.polarity_scores(text)

def analyze_white_paper(text):
    sentences = sent_tokenize(text)
    keywords = [word_tokenize(sentence) for sentence in sentences]
    return keywords

# Нові тексти для аналізу
news = [
    "Good news about stock market", 
    "Bad news about stock market",
    "The economy is booming with unprecedented growth.",
    "The recent scandal has negatively impacted the company's reputation."
]
sentiments = [analyze_sentiment(news_item) for news_item in news]
print(sentiments)

# Додатковий текст для аналізу white papers
white_paper_text = "This is a sample white paper text. Here is another sentence."
keywords = analyze_white_paper(white_paper_text)
print(keywords)

