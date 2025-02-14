import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Taking input from the data
dataset1 = pd.read_csv("dataset.csv")

# Building the pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# model training
X, y = dataset1["email_text"], dataset1["category"]
model.fit(X, y)

# Saving the model in pickle file for future uses
with open("email_classifier.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")
