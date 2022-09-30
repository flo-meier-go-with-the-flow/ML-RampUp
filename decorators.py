import numpy as np
import time

#class Person:
#    def __init__(self):



def time_it(func):
    def wrapper(*args, **kwargs):
        start= time.time()
        func(*args, **kwargs)
        end= time.time()
        time_used= (end - start)*1000 #in ms
        print(f'Time used is {time_used} ms')
    return wrapper

@time_it
def squares(num):
    # compute first n squares
    list1 = []
    for i in range(num):
        list1.append(i ** 2)
    return list1

@time_it
def cubes(num):
    # compute first n squares
    list1 = []
    for i in range(num):
        list1.append(i ** 2)
    return list1


if __name__ == '__main__':
    n = 10 ** 5
    a = squares(n)
    b = cubes(n)

    sli= slice(0,100,10)
    c=np.arange(10000)
    print(c[sli])
