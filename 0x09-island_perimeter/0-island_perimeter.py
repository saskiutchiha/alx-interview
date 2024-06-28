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
            
                if grid[i-1][j] == 0:
                    per+=1
                if grid[i][j-1] == 0:
                    per+=1
                if grid[i][j+1] == 0:
                    per+=1
                if grid[i+1][j] == 0:
                    per+=1
    return per
