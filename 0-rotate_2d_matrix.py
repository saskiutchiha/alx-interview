def dd_matrix(L):
    A = [i[:] for i in L]
    
    for i in range(len(A)):
        for k in range(len(A[i])):
          L[k][-i-1] = A[i][k]
L = [[1,2,3],[4,5,6],[7,8,9]]
dd_matrix(L)
print(L)
