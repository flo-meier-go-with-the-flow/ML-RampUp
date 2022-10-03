import pickle
import numpy as np

def load_mnist_data():
    mnist = pickle.load( open( "mnist.p", "rb" ) )
    X,y=mnist['data'], mnist['target']
    y = y.astype(np.uint8)
    X_train, X_test, y_train, y_test = X[:60000], X[60000:],y[:60000],y[60000:]
    return X_train,X_test, y_train,y_test





