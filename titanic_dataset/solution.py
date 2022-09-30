import os
import urllib.request
from typing import Any

import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextFileReader
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

TITANIC_PATH = os.path.join("datasets", "titanic")
DOWNLOAD_URL = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/titanic/"


def fetch_titanic_data(url=DOWNLOAD_URL, path=TITANIC_PATH):
    if not os.path.isdir(path):
        os.makedirs(path)
    for filename in ("train.csv", "test.csv"):
        filepath = os.path.join(path, filename)
        if not os.path.isfile(filepath):
            print("Downloading", filename)
            urllib.request.urlretrieve(url + filename, filepath)


def load_titanic_data(filename, titanic_path=TITANIC_PATH):
    csv_path = os.path.join(titanic_path, filename)
    return pd.read_csv(csv_path)


fetch_titanic_data()


train_data = load_titanic_data("train.csv")
test_data = load_titanic_data("test.csv")

train_data = train_data.set_index("PassengerId")
test_data = test_data.set_index("PassengerId")


train_data["AgeBucket"] = train_data["Age"] // 5 * 5
#cap the buckets at 60
train_data['AgeBucket']=train_data['AgeBucket'].apply(lambda x: min(x,60.0))

train_data['num_relatives']=train_data['SibSp']+train_data['Parch']
#cap the buckets at 60
train_data['num_relatives']=train_data['num_relatives'].apply(lambda x: min(x,4))

#print(train_data[['num_relatives','Survived']].groupby(['num_relatives']).count())




num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
cat_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("cat_encoder", OneHotEncoder(sparse=False)),
])

num_attribs = ['Age', "Fare"]
cat_attribs = ['num_relatives',"Pclass", "Sex", "Embarked", 'AgeBucket']

preprocess_pipeline = ColumnTransformer([("num", num_pipeline, num_attribs), ("cat", cat_pipeline, cat_attribs),
                                         ])

X_train = preprocess_pipeline.fit_transform(train_data[num_attribs + cat_attribs])
y_train = train_data["Survived"]


forest_clf = RandomForestClassifier(n_estimators=100, random_state=42)
forest_scores = cross_val_score(forest_clf, X_train, y_train, cv=10)
print(forest_scores.mean())


svm_clf = SVC(gamma="auto")
svm_scores = cross_val_score(svm_clf, X_train, y_train, cv=10)
print(svm_scores.mean())


param_grid = [{'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf', 'poly']}]

svc = SVC()
grid_search = GridSearchCV(svc, param_grid, cv=5, return_train_score=True)
grid_search.fit(X_train, y_train)
cvres = grid_search.cv_results_

df_cvres = pd.DataFrame(cvres['mean_test_score'], index=cvres['params'], columns=['mean_test_score'])
df_cvres['mean_train_score'] = cvres['mean_train_score']
print(df_cvres)
