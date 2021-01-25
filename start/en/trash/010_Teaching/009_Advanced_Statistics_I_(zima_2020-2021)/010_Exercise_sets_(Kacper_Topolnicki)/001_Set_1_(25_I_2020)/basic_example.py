#!/usr/bin/env python

import numpy

a = numpy.array([1 , 0 , 0 , 1] , dtype = numpy.float32)

print("a.shape : " , a.shape)
print("a.dtype : " , a.dtype)

b = numpy.array([0 , -1 , 1 , 0] , dtype = numpy.float32)

print("b.shape : " , b.shape)
print("b.dtype : " , b.dtype)


print("2.0 * a : " , 2.0 * a)
print("2.0 * b : " , 2.0 * b)

aMat = a.reshape((2 , 2))
bMat = b.reshape((2 , 2))

print("aMat.shape : " , aMat.shape)
print("aMat.dtype : " , aMat.dtype)
print("aMat : " , aMat)

print("bMat.shape : " , bMat.shape)
print("bMat.dtype : " , bMat.dtype)
print("bMat : " , bMat)

print("aMat * aMat : " , aMat * aMat)
print("bMat * bMat : " , bMat * bMat)

print("numpy.matmul(aMat , aMat) : " , numpy.matmul(aMat , aMat))
print("numpy.matmul(bMat , bMat) : " , numpy.matmul(bMat , bMat))
print("numpy.matmul(aMat , bMat) : " , numpy.matmul(aMat , bMat))
print("numpy.matmul(bMat , aMat) : " , numpy.matmul(bMat , aMat))
