from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap
import numpy as np
import random
from scipy import stats

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
X_train, X_test, y_train, y_test = train_test_split(Xm, ym, test_size=0.25)

dct_clf = DecisionTreeClassifier()

param_grid = {'max_leaf_nodes': [3, 10, 30, 100]}

best_dct_clf = DecisionTreeClassifier(max_leaf_nodes=30)
estimator_list = []
score_list = []
predict_list=[]
indices = np.array([random.randint(0, 7499) for i in range(0, 100 * 1000)]).reshape(1000, 100)
for index in range(0, indices.shape[0]):
    X = X_train[indices[index]]
    y = y_train[indices[index]]
    best_dct_clf = DecisionTreeClassifier(max_leaf_nodes=30)
    best_dct_clf.fit(X, y)
    y_predict = best_dct_clf.predict(X_test)
    predict_list.append(y_predict)
    score_list.append(accuracy_score(y_test, y_predict))
forest_predict=stats.mode(np.array(predict_list), axis=0, keepdims=False)
print(forest_predict[0])
print(accuracy_score(y_test,forest_predict[0]))
# plot_prediction(X_train,y_train,best_dct_clf)

# print(Xm,ym)
