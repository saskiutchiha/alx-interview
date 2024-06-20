#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
   """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
   """
   nbr = 0
   coins = sorted(coins)[::-1]
   while (total <= 0):
      if total - coins[0] >=0:
         total-=coins[0]
        
         nbr +=1
      else :
        if len(coins) > 1 :
         coins = coins[1:]
        else :
          return -1
      
   return nbr
