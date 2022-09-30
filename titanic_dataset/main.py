from titanic_dataset.load_data import fetch_titanic_data, load_titanic_data
from preprocessing import preprocessing





from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_validate
from sklearn.svm import SVC

fetch_titanic_data()
train_data = load_titanic_data("train.csv")
test_data = load_titanic_data("test.csv")

# preprocessing parameters
embarked_onehot = False
pclass_onehot = False
train_data, y_train = preprocessing(train_data, embarked_onehot=embarked_onehot, pclass_onehot=pclass_onehot)

X_train = train_data.to_numpy()

std_sc_bool=True
if std_sc_bool:
    std_sc=StandardScaler()
    X_train=std_sc.fit_transform(X_train)

ridge_clf=RidgeClassifier(alpha=1)
scores = cross_validate(ridge_clf, X_train, y_train, cv=5,return_train_score=True)
print('Ridge train:', scores['train_score'].mean(),scores['train_score'].std())
print('Ridge test:', scores['test_score'].mean(),scores['test_score'].std())


log_reg=LogisticRegression()
scores = cross_validate(log_reg, X_train, y_train, cv=5, return_train_score=True)
print('LogReg train:', scores['train_score'].mean(),scores['train_score'].std())
print('LogReg test:', scores['test_score'].mean(),scores['test_score'].std())

rand_for=RandomForestClassifier(max_depth=2)
scores = cross_validate(rand_for, X_train, y_train, cv=5,return_train_score=True)
print('RandFor train:', scores['train_score'].mean(),scores['train_score'].std())
print('RandFor test:', scores['test_score'].mean(),scores['test_score'].std())

svc=SVC(kernel='rbf', C=1.0)
scores = cross_validate(svc, X_train, y_train, cv=5, return_train_score=True)
print('SVC train:', scores['train_score'].mean(),scores['train_score'].std())
print('SVC test:', scores['test_score'].mean(),scores['test_score'].std())


















