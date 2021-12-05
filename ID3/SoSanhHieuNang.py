import ID3
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

df = pd.read_csv('weather.csv', index_col = 0, parse_dates = True)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
tree = ID3.DecisionTreeID3(max_depth = 3, min_samples_split = 2)
tree.fit(X, y)
print(tree.predict(X))
