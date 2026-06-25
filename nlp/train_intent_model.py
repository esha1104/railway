import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

training_data = [
    ("show salary", "salary"),
    ("salary details", "salary"),
    ("show payslip", "salary"),
    ("view salary slip", "salary"),
    ("display salary", "salary"),

    ("salary history", "salary_history"),
    ("past salaries", "salary_history"),
    ("salary records", "salary_history"),
    ("show previous salary", "salary_history"),

    ("pf details", "pf"),
    ("show pf balance", "pf"),
    ("provident fund", "pf"),
    ("pf information", "pf"),

    ("pf history", "pf_history"),
    ("pf transactions", "pf_history"),
    ("show pf records", "pf_history"),

    ("contact hr", "hr"),
    ("hr details", "hr"),
    ("personnel department", "hr"),
    ("human resources", "hr"),

    ("restart", "restart"),
    ("start over", "restart"),
    ("reset chatbot", "restart"),
]

texts = [x[0] for x in training_data]
labels = [x[1] for x in training_data]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

model = LogisticRegression()

model.fit(X, labels)

with open("intent_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Intent model trained successfully")