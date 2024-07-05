#!/usr/bin/python3
"""Prime game module.
"""


def prime_number(n):
    """determine if a number n is a prime number"""
    if n == 1:
        return False
    for i in range(1,n):
        if i != 1 and i != n :
            if n%i == 0:
                return False
    return True
def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    win = 0
    players = [('Maria','Ben'),[0,0]]
    for i in nums:
        for j in range(1,i+1):
            if prime_number(j):
                win +=1
        if win%2 == 0:
            players[1][1]+=1
        else :
            players[1][0]+=1
        win = 0
    return players[0][players[1].index(max(players[1]))]
            

