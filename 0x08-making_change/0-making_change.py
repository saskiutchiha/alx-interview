#!/bin/usr/python3

""" Contains makeChange function"""


def makeChange(coins, total):
  """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
   nbr = 0
   coins = sorted(coins)[::-1]
   while (total != 0):
      if total - coins[0] >=0:
         total-=coins[0]
        
         nbr +=1
      else :
        if len(coins) > 1 :
         coins = coins[1:]
        else :
          return -1
      
   return nbr
print(makeChange([1256, 54, 48, 16, 102], 1453))
