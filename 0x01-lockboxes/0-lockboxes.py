#!/usr/bin/python3

"""Solves the lock boxes puzzle """

def unlock(L,li,indice =0):
  """
  This function is used to unlock the boxes.
    
  Args:
        L (list): List of boxes with keys.
        li (list): List of boxes status, 1 indicates the box is unlocked, 0 indicates the box is locked.
        indice (int, optional): The index of the box to start with. Defaults to 0.
        
  Returns:
    None
  """
  if L[indice] != [] :
      for key in L[indice]:
       if li[key] != 1:
        li[key] = 1
        unlock(L,li,key)
def canUnlockAll(L):
 """
 This function checks if all boxes can be unlocked.
    
 Args:
    L (list): List of boxes with keys.
        
 Returns:
        bool: True if all boxes can be unlocked, otherwise False.
 """
 li = [1] + [0]*(len(L)-1)
 unlock(L,li)
 if 0 in li :
   return False
 else :
   return True
