from numpy import array 
from numpy import mean
from numpy import cov
from numpy.linalg import eig

A=array([[1,2,3],[3,4,5],[3,6,2]])
print('Original Matrix A:')
print(A)
M=mean(A.T,axis=1)
C=A-M
V=cov(C.T)
values,vectors = eig(V)
print('Vectors:')
print(vectors)
P=vectors.T.dot(C.T)
print('Projection of A')
print(P.T)