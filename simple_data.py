import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

def create_data(number_samples_per_class=200, number_features=3):
    class1 = np.zeros((number_samples_per_class, number_features))
    label1 = np.zeros(number_samples_per_class)
    ones_features = 1
    class2 = np.zeros((number_samples_per_class, number_features))
    label2 = np.ones(number_samples_per_class)
    ones = np.ones(number_samples_per_class)
    for i in range(ones_features):
        class2[:, i] = ones
    X = np.concatenate((class1, class2))
    y = np.concatenate((label1, label2))
    noise = np.random.rand(2 * number_samples_per_class, 3) * 2 - 1
    X = X + noise
    return X,y

def print_grid_search_scores(estimator, param_grid, X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    grid_search = GridSearchCV(estimator, param_grid, cv=5, scoring='accuracy', return_train_score=True)
    grid_search.fit(X_train, y_train)
    cv_res = grid_search.cv_results_

    cv_DF = pd.DataFrame(cv_res['mean_test_score'], columns=['mean_test_score'], index=cv_res['params'])
    # cv_DF['params']= cv_res['params']
    cv_DF['mean_train_score'] = cv_res['mean_train_score']
    print(estimator, ' scores:')
    print(cv_DF)
    return None

if __name__ == '__main__':
    number_samples_per_class = 200
    number_features = 3
    X,y = create_data(number_samples_per_class,number_features)


    param_grid = [{'n_neighbors': [3, 5, 7, 10, 15, 30]}]
    knc = KNeighborsClassifier()
    print_grid_search_scores(estimator=knc, param_grid=param_grid,X=X,y=y)


    ridge_clf = RidgeClassifier()
    param_grid = [{'alpha': [0.01, 0.1, 1]}]
    print_grid_search_scores(estimator=ridge_clf, param_grid=param_grid, X=X, y=y)
