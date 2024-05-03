def unlock(L,li,indice =0):
  if L[indice] != [] :
      for key in L[indice]:
       if li[key] != 1:
        li[key] = 1
        unlock(L,li,key)
def canUnlockAll(L):
 li = [1] + [0]*(len(L)-1)
 unlock(L,li)
 if 0 in li :
   return False
 else :
   return True
