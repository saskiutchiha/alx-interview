#!/usr/bin/python3
"""2D matrix rotation module.
"""

def dd_matrix(L):
    A = [i[:] for i in L]
    
    for i in range(len(A)):
        for k in range(len(A[i])):
          L[k][-i-1] = A[i][k]
