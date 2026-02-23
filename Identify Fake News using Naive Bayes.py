#import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

#load dataset
data = pd.read_csv('d:/python_ka_chilla/AI Projects/Identify Fake News using Naive Bayes/fake_news.csv')
# display first few rows of the dataset
print(data.head())

#missing values check
print("\nMissing Values in Each Column:\n", data.isnull().sum())
#fill missing values if any
data = data.dropna()
#define features and labels
X = data['text']
y = data['label']  # 'FAKE' or 'REAL'

#split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#vectorize the text data using Count Vectorizer
vectorizer = CountVectorizer(stop_words='english')
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

#train a Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vectors, y_train)

#make predictions on the test set
y_pred = model.predict(X_test_vectors)

#evaluate the model
print("Model Evaluation Results:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
