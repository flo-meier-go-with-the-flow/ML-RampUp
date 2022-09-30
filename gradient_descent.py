import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def load_bin_dataset():
    iris = datasets.load_iris()
    x = iris["data"][:, (2, 3)]  # petal length, petal width
    y = iris["target"]

    setosa_or_versicolor = (y == 0) | (y == 1)
    x = x[setosa_or_versicolor]
    y = y[setosa_or_versicolor]
    return x, y


def load_dataset():
    iris = datasets.load_iris()
    x = iris["data"][:, (2, 3)]  # petal length, petal width
    y = iris["target"]
    return x, y


def add_constant_feature(X_data):
    x_const = np.ones((X_data.shape[0], 1))
    X_data = np.concatenate((X_data, x_const), axis=1)
    return X_data


def logistic_function(x):
    return 1 / (1 + np.exp(-x))


def compute_log_loss(X, y, params):
    # y should have shape nx1
    num_samples = X.shape[0]
    linear_trans = X.dot(params)
    logistic = logistic_function(linear_trans)
    loss = y * np.log(logistic) + (1 - y) * np.log(1 - logistic)
    return -loss.sum(axis=0) / num_samples


def compute_gradient_of_log_loss(X, y, params):
    # y should have shape nx1
    num_samples = X.shape[0]
    linear_trans = X.dot(params)
    logistic = logistic_function(linear_trans)
    return X.T.dot(logistic - y) / num_samples


def compute_cross_entropy_loss(X, y, params):
    num_samples = X.shape[0]
    s_k = X.dot(params)  # m x k
    p_k = np.exp(s_k) / np.exp(s_k).sum(axis=1).reshape(y.shape[0], 1)  # m x k
    log_p_k = np.log(p_k)
    sum = 0.0
    y_vect = y.reshape(y.shape[0])
    for y_value in np.unique(y):
        sum -= log_p_k[y_vect == y_value, y_value].sum(axis=0) / num_samples
    return sum


def compute_gradient_of_cross_entropy_loss(X, y, params):
    num_classes = params.shape[1]
    gradient = np.zeros(params.shape)
    num_samples = X.shape[0]
    s_k = X.dot(params)  # m x k
    p_k = np.exp(s_k) / np.exp(s_k).sum(axis=1).reshape(y.shape[0], 1)  # m x k
    for i in range(0, num_classes):
        a = p_k[:, i:i + 1]
        b = (y == i).astype(float)
        gradient_k = ((p_k[:, i:i + 1] - (y == i).astype(float)) * X).sum(axis=0)/num_samples
        gradient[:, i] = gradient_k.T
    return gradient

def gradient_descent(X, y, compute_loss, compute_gradient, num_epoches=100, learning_rate=1.0, bool_log_reg=True):
    if bool_log_reg:
        num_classes = 1
    else:
        num_classes = np.unique(y).size
    params = np.zeros((X_train.shape[1], num_classes))
    training_loss = np.zeros(num_epoches)
    y_mat = y.reshape(y_train.shape[0], 1)
    for i in range(0, num_epoches):
        loss = compute_loss(X, y_mat, params)
        print(f'Loss in epoch {i}: {loss}')
        training_loss[i] = loss
        gradient = compute_gradient(X, y_mat, params)
        params -= learning_rate * gradient
        print(f'new params: {params}')
    return params, training_loss


if __name__ == '__main__':
    # X_data, y_data = load_bin_dataset()
    X_data, y_data = load_dataset()
    X_data = add_constant_feature(X_data)
    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.25)

    # loss=compute_log_loss(X_train,y_train.reshape(y_train.shape[0],1),params)
    # gradient = compute_gradient_of_log_loss(X_train,y_train.reshape(y_train.shape[0],1),params)
    num_epoches = 5000

    learning_rate = 0.01
    params, training_loss = gradient_descent(X_train, y_train, compute_cross_entropy_loss,
                                             compute_gradient_of_cross_entropy_loss,
                                             num_epoches=num_epoches, learning_rate=learning_rate, bool_log_reg=False)

    fig, ax = plt.subplots()
    ax.plot(np.arange(0, num_epoches), training_loss)
    plt.show()
