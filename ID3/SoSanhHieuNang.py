from ID3 import DecisionTreeID3
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from time import time

# Input data
pima = pd.read_csv('diabetes.csv', header=0)
X = pima.drop(["Outcome"], axis=1)  # Features
y = pima['Outcome']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Thuat toan tu viet
start_time = time()
tree = DecisionTreeID3(max_depth=5, min_samples_split=2)
tree.fit(X_train, y_train)
y_predict = tree.predict(X_test)
end_time = time()

# Su dung thu vien co san
start_time2 = time()
tree2 = DecisionTreeClassifier(criterion="entropy", max_depth=5, min_samples_split=2)
tree2.fit(X_train, y_train)
y_predict2 = tree2.predict(X_test)
end_time2 = time()

print("Do chinh xac cua thuat toan tu cai dat:")
print(classification_report(y_test, y_predict))
print("Thoi gian chay:", end_time - start_time)
print("__________________________")
print("Do chinh xac cua thuat toan cua scikit-learn:")
print(classification_report(y_test, y_predict2))
print("Thoi gian chay:", end_time2 - start_time2)

