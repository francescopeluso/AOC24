#
#   Advent of Code 2024 - Day 16
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

from collections import deque
import math

def read_input():
  with open('input.txt') as f:
    return [list(row) for row in f.read().splitlines()]

def find_start_end(grid):
  start = end = None
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == 'S':
        start = (y, x)
      elif grid[y][x] == 'E':
        end = (y, x)
  return start, end

DIRECTIONS = {
  "^": (["<", ">"], (-1, 0)),
  ">": (["^", "v"], (0, 1)),
  "v": (["<", ">"], (1, 0)),
  "<": (["^", "v"], (0, -1))
}


def solve_maze(grid):
  start, end = find_start_end(grid)
  if not start or not end:
    return float('inf'), set()

  values = []
  for i in range(len(grid)):
    values.append([])
    for j in range(len(grid[i])):
      values[i].append({
        ">": (math.inf, set()),
        "v": (math.inf, set()),
        "<": (math.inf, set()),
        "^": (math.inf, set())
      })
  
  queue = deque([(start[0], start[1], ">", 0, {start})])
  
  while queue:
    y, x, direction, cost, path = queue.popleft()
    
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]) or grid[y][x] == '#':
      continue
        
    path.add((y, x))
    current_min, current_path = values[y][x][direction]
    
    if current_min < cost:
      continue
    elif current_min == cost:
      current_path.update(path)
    else:
      current_path.clear()
      current_path.update(path)
      values[y][x][direction] = (cost, current_path)
    
    if (y, x) == end:
      continue
        
    rotations, (dy, dx) = DIRECTIONS[direction]
    queue.append([y + dy, x + dx, direction, cost + 1, set(path)])
    for new_dir in rotations:
      queue.append([y, x, new_dir, cost + 1000, set(path)])
  
  min_cost = math.inf
  best_path = set()
  for direction_data in values[end[0]][end[1]].values():
    cost, path = direction_data
    if cost < min_cost:
      min_cost = cost
      best_path = path
  
  return min_cost, best_path


def first_part():
  grid = read_input()
  min_cost, _ = solve_maze(grid)
  return min_cost


def second_part():
  grid = read_input()
  _, tiles = solve_maze(grid)
  return len(tiles)


if __name__ == "__main__":
  print("First part:", first_part())
  print("Second part:", second_part())