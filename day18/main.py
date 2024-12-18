#
#   Advent of Code 2024 - Day 18
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

ROWS = 71
COLS = 71

def read_input():
  total = []
  with open('input.txt') as f:
    total = [[int(x) for x in line.strip().split(',')] for line in f]
  
  return total[:1024], total[1024:]
  

def print_map(map):
  print()
  for row in map:
    print(''.join(row))
  print()
  

def generate_map(bytes):
  map = []
  for i in range(ROWS):
    row = []
    for j in range(COLS):
      if [j, i] in bytes:
        row.append('#')
      else:
        row.append('.')
    map.append(row)
  return map


def path_to_exit(map):
  queue = [(0, 0, [(0, 0)])]
  visited = set([(0, 0)])
  
  while queue:
    row, col, path = queue.pop(0)
    
    if row == ROWS-1 and col == COLS-1:
      for r, c in path:
        map[r][c] = 'o'

      return path
        
    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
      new_row, new_col = row + dr, col + dc
      
      if (0 <= new_row < ROWS and 0 <= new_col < COLS and map[new_row][new_col] != '#' and (new_row, new_col) not in visited):
        visited.add((new_row, new_col))
        queue.append((new_row, new_col, path + [(new_row, new_col)]))

  return []


def find_cutoff_coords(map, cutoffs):
  for cutoff in cutoffs:
    x, y = cutoff
    if map[y][x] == 'o':
      temp_map = [row[:] for row in map]
      temp_map[y][x] = '#'
      
      alternative_path = path_to_exit(temp_map)
      
      if not alternative_path:
        return [x, y]
      else:
        map = temp_map
        
  return None


def first_part():
  bytes, cutoffs = read_input()
  map = generate_map(bytes)
  path = path_to_exit(map)
  
  print_map(map)
  return len(path) - 1 if path else None


def second_part():
  bytes, cutoffs = read_input()
  map = generate_map(bytes)
  path = path_to_exit(map)

  return find_cutoff_coords(map, cutoffs)


if __name__ == "__main__":
  print("First part:", first_part())
  print("Second part:", second_part())