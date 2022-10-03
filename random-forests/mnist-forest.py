import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

from load_data import load_mnist_data



def knc_grid_search(param_grid=[{'n_neighbors':[3,5],'weights':['uniform','distance']}]):
    param_grid=param_grid
    knc = KNeighborsClassifier()

    grid_search = GridSearchCV(knc, param_grid, cv=5, scoring='accuracy', return_train_score=True)
    grid_search.fit(X_train, y_train)
    cv_res=grid_search.cv_results_
    return cv_res

def print_scores(cv_res):
    cv_res=cv_res
    knc_cv_DF=pd.DataFrame(cv_res['mean_test_score'], columns=['mean_test_score'],index = cv_res['params'])
    #cv_DF['params']= cv_res['params']
    knc_cv_DF['mean_train_score']= cv_res['mean_train_score']
    print(knc_cv_DF)
    return knc_cv_DF



#
# param_grid=[{'n_neighbors':[3,5],'weights':['uniform','distance']}]
# cv_res= knc_grid_search(param_grid)
# print_scores(cv_res)

if __name__=='__main__':
    X_train,X_test,y_train,y_test=load_mnist_data()
    print(X_train.shape)