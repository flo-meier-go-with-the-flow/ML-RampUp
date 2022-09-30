import numpy as np

a=np.arange(0,100,1)
b=a.reshape(10,10)
c=b.astype(float)
print(b.shape)
print(b.strides)
b[0,0]=100
#print(b)
#print(a)
c=c.flatten




a1 = np.arange(0,100,1).reshape(10,10)
a2 = np.flip(np.arange(0,100,1)).reshape(10,10)
print(a1 >= a2)
print(a2)
print(a2.argmax(axis=1))
print(a2.all(axis=1))

