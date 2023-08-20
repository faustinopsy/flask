import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv("./base.csv")

df = df[["text_pt", "sentiment"]]

df = df[df["sentiment"].isin(["pos", "neg"])]

texts = df["text_pt"].tolist()
labels = df["sentiment"].tolist()

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
y = labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

joblib.dump(model, 'sentiment_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print(classification_report(y_test, y_pred))
