from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap
import numpy as np


def plot_prediction(x_train, y_train, estimator):
    plt.figure(figsize=(10, 4))
    plt.plot(x_train[y_train == 1, 0], x_train[y_train == 1, 1], 'b.', markersize=2, label='class 1')

    plt.plot(x_train[y_train == 0, 0], x_train[y_train == 0, 1], 'y.', markersize=2, label='class 0')

    x0, x1 = np.meshgrid(
        np.linspace(-3, 3, 100).reshape(-1, 1),
        np.linspace(-3, 3, 100).reshape(-1, 1),
    )
    x_new = np.c_[x0.ravel(), x1.ravel()]
    y_predict = estimator.predict(x_new)
    zz = y_predict.reshape(x0.shape)

    custom_cmap = ListedColormap(['#fafab0', '#9898ff'])

    plt.contourf(x0, x1, zz, cmap=custom_cmap)
    plt.show()


Xm, ym = make_moons(n_samples=10000, noise=0.4)
X_train, X_test, y_train, y_test = train_test_split(Xm, ym)

dct_clf = DecisionTreeClassifier()

param_grid = {'max_leaf_nodes': [3, 10, 30, 100]}

grid_search = GridSearchCV(dct_clf, param_grid, cv=4, return_train_score=True)
grid_search.fit(X_train, y_train)
results = grid_search.cv_results_
print(grid_search.cv_results_.keys())

res_df = pd.DataFrame(index=results['params'])
res_df['mean_test_score'] = grid_search.cv_results_['mean_test_score']
res_df['mean_train_score'] = grid_search.cv_results_['mean_train_score']
print(res_df)

best_dct_clf = DecisionTreeClassifier(max_leaf_nodes=30)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25)
best_dct_clf.fit(X_train, y_train)
accuracy_val = accuracy_score(y_val, best_dct_clf.predict(X_val))
accuracy_train = accuracy_score(y_train, best_dct_clf.predict(X_train))
print(f'dct accuracy score val: {accuracy_val}, train: {accuracy_train}')

plot_prediction(X_train,y_train,best_dct_clf)

# print(Xm,ym)
