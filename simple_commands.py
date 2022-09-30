first = 'Flo'
last = 'Bär'


def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


full_name = get_full_name(
    first_name=first,
    last_name=last,
    formatter=lambda first_name, last_name: f'{first_name} {last_name}'
)

print(full_name)


def times(n):
    """Returns the function that multiplies by n"""
    return lambda x: x * n


ten_times = times(10)
print(round(ten_times(3.14), 2))

companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

companies.sort(key=lambda x: x[2], reverse=True)
print(companies)

list1 = range(0, 100, 5)
print(list(list1))

list2 = []
for i in range(0, 100, 5):
    list2.append(i)


def fn(element, threshold=50):
    return element > threshold


print(list(filter(fn, list2)))


def triple(number):
    return number, number + 1, number + 2


print(list(map(triple, list1)))


def quatrupel(number):
    return number, number + 1, number + 2, number + 3


countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

print(list(filter(lambda x: x[1] > 300_000_000, countries)))

print([country for country in countries if country[1] > 300_000_000])

print([country for country in countries if len(country[0])> 6])


keywords=['Sport', 'Tennis', 'Soccer']

for i, keyword in enumerate(keywords):
    print(i, keyword)


from collections import Counter

letter_count=Counter('Hello my name is Flo')
letter_count.update('Hi my name is Joe')
print(letter_count)


# letter_dict= {'h':1, 'o':5, 'i':3}
for key, value in letter_count.items():
    print(f'{key} : {value}')

print(letter_count.most_common(4))

#least common objects
print(letter_count.most_common()[:-6:-1])


l1=list('My name is Flo')
l1.reverse()
l2=[0,1,2,3,4]
l2=list(reversed(l2))
print(l1)
print(l2)
a=l2[-1::-1]
b=l2
a[0]=9
b[0]=9
print(l2)
print(a)
print(b)
print(l1[-1:3:-1]) # start:stop:step
print(l2[5::-1])
print(l2)
print(list(range(5,-1,-1)))
print([l2[i] for i in range(4,-1,-1)]) #list comprehension

import numpy as np
print(type(np.arange(100,10,-10)))
a=np.ones((100,2))
b= np.zeros((100,3))
c=np.concatenate((a,b), axis=1)
d=np.ones((100,1))*2
e=np.arange(0,100,1)
f=np.arange(1,11).reshape(10,1)
indeciss=(e<10)
print(c[indeciss]/f.shape[0])
print(c[:,1:2])

print((e==1).astype(float))

X=np.arange(0,100).reshape(100,1)
from sklearn.model_selection import ShuffleSplit


rs=ShuffleSplit(n_splits=100, train_size=10, test_size=10)
for train_index, test_index in rs.split(X):
    print('Train:',train_index, X[train_index])


