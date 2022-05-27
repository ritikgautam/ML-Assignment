# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Q_H-hxm13-aJVBmkSvUBBNsJYu5bI4K
"""

# Import Libraries that we need 
import numpy as np
from numpy import log
from numpy.linalg import inv as inverse, det as determinant

# Given input
n = 3
data = [
        # 𝜔1
        np.array([
            [-5.01, -8.12, -3.68],
            [-5.43, -3.48, -3.54],
            [1.08, -5.52, 1.66],
            [0.86, -3.78, -4.11],
            [-2.67, 0.63, 7.39],
            [4.94, 3.29, 2.08],
            [-2.51, 2.09, -2.59],
            [-2.25, -2.13, -6.94],
            [5.56, 2.86, -2.26],
            [1.03, -3.33, 4.33]
        ]),
        # 𝜔2
        np.array([
            [-0.91, -0.18, -0.05],
            [1.30, -2.06, -3.53],
            [-7.75, -4.54, -0.95],
            [-5.47, 0.50, 3.92],
            [6.14, 5.72, -4.85],
            [3.60, 1.26, 4.36],
            [5.37, -4.63, -3.65],
            [7.18, 1.46, -6.66],
            [-7.39, 1.17, 6.30],
            [-7.50, -6.32, -0.31]

        ]),

        # 𝜔3
        np.array([
            [5.35, 2.26, 8.13],
            [5.12, 3.22, -2.66],
            [-1.34, -5.31, -9.87],
            [4.48, 3.42, 5.19],
            [7.11, 2.39, 9.21],
            [7.17, 4.33, -0.98],
            [5.75, 3.97, 6.65],
            [0.77, 0.27, 2.41],
            [0.90, -0.43, -8.71],
            [3.52, -0.36, 6.43]
        ])
    ]

#find mean
mean = []
for i in range(len(data)):
  mean.append([sum(x)/len(x) for x in zip(*data[i])])
mean = np.array(mean)

#find covariance
covariance = []
for i in range(len(data)):
    covariance.append(np.cov(data[i].T))
covariance = np.array(covariance)

P = [1/2, 1/2, 0]

#The discriminant function is given below
def discriminant_function(i: int, x: np.array, P: list):
    if P[i] == 0:
        return -np.inf

    # finding dimension of input x
    dimention = x.shape[0]
    # Get the mean values based on given dimention
    mean_dimention = mean[:, 0:dimention]
    # Get the covariance values based on given dimention
    covariance_dimention = covariance[:, 0:dimention, 0:dimention]
    temp = np.matmul(inverse(covariance_dimention[i]), (x - mean_dimention[i]))
    #discriminant function
    res = -0.5 * np.matmul((x - mean_dimention[i]).T, temp) -0.5 * dimention * log(2 * np.pi)\
     - 0.5 * log(determinant(covariance_dimention[i]))
     + log(P[i])
    return res

# Now, check for all data points using above discriminant function
for i in range(n):
    print("\n")
    print("CLASS 𝜔%d" % (i + 1))
    print("."*12)
    for x in data[i]:
        print("Discriminant values for", x, end='\t')
        for i in range(n):
            print("𝜔%d : %.3f\t" % (i+1, discriminant_function(i, x, P)), end=' ')
        print()