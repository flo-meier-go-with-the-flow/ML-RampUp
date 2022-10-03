import pickle
from sklearn.datasets import fetch_openml

mnist=fetch_openml('mnist_784',version=1)
pickle.dump(mnist, open("mnist.p", "wb"))
