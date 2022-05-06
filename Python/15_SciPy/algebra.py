import numpy as np
from scipy.integrate import quad
from scipy.integrate import dblquad
from scipy.integrate import nquad

def f(x):
    return x
area=quad(f,0,2)
print(area)


def f(x):
    return x*y
area=dblquad(f,0,2,0,5)
print(area)


f=lambda x,y:x*y
ylb=lambda y:y
ylb=lambda y:y*5
area=dblquad(f,0,2,ylb,yub)
print(area)


def f(x,y,z):
    return x*y*z
area=nquad( f,[[0,2],[0,3],[0,4]] )
print(area)


from scipy import linalg
a=np.array([[3,2,5],[1,-1,2]])
b=np.array([[2],[4]])
x,resid,rank,sigma=linalg.lstsq(a,b)
print(x)


x=np.array([[3,2],[1,-1]])
print(linalg.inv(x))



print(linalg.det(x))



from scipy.fftpack import fft,ifft
x=np.array([1,2,3,4])
y=fft(x)
print(y)


from scipy.fftpack import fft,ifft
x=np.array([1,2,3,4])
y=ifft(x)
print(y)

