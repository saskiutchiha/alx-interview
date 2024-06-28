#!/usr/bin/python3
"""Island perimeter computing module.
"""

def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    per = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
         if grid[i][j] == 1:
            if i == 0 or j == 0 or i == len(grid) or j == len(grid[i]) : 
                if j == 0 :
                    if i == 0:
                     if grid[i+1][j] == 0:
                        per = per + 1
                    elif i == len(grid) -1:
                        if grid[i-1][j] == 0:
                         per = per + 1
                    else :
                       if grid[i+1][j] == 0:
                        per = per + 1
                       if grid[i-1][j] == 0:
                         per = per + 1
                    if grid[i][j+1] == 0:
                        per = per + 1
                       
                elif j == len(grid[i]-1):
                    if i == 0 :
                       if grid[i+1][j] == 0:
                        per = per + 1
                    if i == len(grid) -1:
                      if grid[i+1][j] == 0:
                        per = per + 1  
                    else :
                       if grid[i+1][j] == 0:
                        per = per + 1
                       if grid[i-1][j] == 0:
                         per = per + 1
                    if grid[i][j-1] == 0:
                        per = per + 1
                elif i == 0 :
                   if grid[i][j-1] == 0:
                        per = per + 1
                   if grid[i][j+1] == 0:
                        per = per + 1
                   if grid[i+1][j] == 0:
                        per = per + 1
                elif i ==  en(grid[i]-1):
                   if grid[i][j-1] == 0:
                        per = per + 1
                   if grid[i][j+1] == 0:
                        per = per + 1
                   if grid[i-1][j] == 0:
                        per = per + 1
                
            else :
                if grid[i-1][j] == 0:
                    per+=1
                if grid[i][j-1] == 0:
                    per+=1
                if grid[i][j+1] == 0:
                    per+=1
                if grid[i+1][j] == 0:
                    per+=1
    return per
print(island_perimeter([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]))