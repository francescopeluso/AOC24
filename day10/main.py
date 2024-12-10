#
#   Advent of Code 2024 - Day 10
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

from collections import deque


def read_input():
  with open('input.txt', 'r') as file:
    return [[int(x) for x in line.strip()] for line in file]


def get_neighbors(x, y, grid):
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  neighbors = []
  height = len(grid)
  width = len(grid[0])
  
  for dx, dy in directions:
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < height and 0 <= new_y < width:
      neighbors.append((new_x, new_y))
  
  return neighbors


def count_paths(start_x, start_y, grid):
  memo = {}
  
  def dfs(x, y, current_height):
    if (x, y, current_height) in memo:
      return memo[(x, y, current_height)]
        
    if grid[x][y] == 9:
      return 1
        
    total_paths = 0
    
    for next_x, next_y in get_neighbors(x, y, grid):
      next_height = grid[next_x][next_y]
      if next_height == current_height + 1:
        total_paths += dfs(next_x, next_y, next_height)
    
    memo[(x, y, current_height)] = total_paths
    return total_paths

  return dfs(start_x, start_y, 0)


def find_trailheads(grid):
  trailheads = []
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 0:
        trailheads.append((i, j))
  return trailheads


def find_reachable_nines(start_x, start_y, grid):
  visited, reachable_nines = set(), set()
  queue = deque([(start_x, start_y, 0)])
  
  while queue:
    x, y, current_height = queue.popleft()
    
    if (x, y) in visited:
      continue
        
    visited.add((x, y))
    
    if grid[x][y] == 9:
      reachable_nines.add((x, y))
      continue
        
    for next_x, next_y in get_neighbors(x, y, grid):
      next_height = grid[next_x][next_y]
      
      if next_height == current_height + 1:
        queue.append((next_x, next_y, next_height))

  return reachable_nines


###


def first_part(grid):
  total_score = 0
  trailheads = find_trailheads(grid)
  
  for x, y in trailheads:
    reachable_nines = find_reachable_nines(start_x=x, start_y=y, grid=grid)
    score = len(reachable_nines)
    total_score += score
      
  return total_score

def second_part(grid):
  total = 0
  trailheads = find_trailheads(grid)
  
  for x, y in trailheads:
    rating = count_paths(x, y, grid)
    total += rating
      
  return total

if __name__ == "__main__":
  grid = read_input()
  
  print("First part result: " + str(first_part(grid)))
  print("Second part result: " + str(second_part(grid)))
  print()