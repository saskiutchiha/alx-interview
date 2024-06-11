#!/usr/bin/python3
import copy as cp
def rotate_2d_matrix(matrix):
    A = cp.deepcopy(matrix)
    
    for i in range(len(A)):
        for k in range(len(A[i])):
          L[k][-i-1] = A[i][k]
