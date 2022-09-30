import random

import numpy as np

X = np.concatenate((np.zeros((100, 1)), np.ones((100, 1)), np.arange(0, 100).reshape(100, 1)), axis=1)

indices = [random.randint(0, 100) for i in range(0, 10)]
print(indices, X[indices])