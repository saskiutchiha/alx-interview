#!/usr/bin/python3
def trinagle(n):
    l = [[1]]
    if n <= 0 :
        return []

    for i in range(1,n):
        l = l + [l[i-1] + [1]]
        j = i-1
        while j > 0:
            l[i][j] = l[i][j] + l[i][j-1]
            j-=1
    return l
