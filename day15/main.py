#
#   Advent of Code 2024 - Day 15
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

from collections import deque

DIRECTIONS = {"<": -1j, ">": 1j, "^": -1, "v": 1}   # this is cool ahah

def read_input():
  with open('input.txt') as f:
    warehouse, movement = f.read().split("\n\n")
  return [list(row) for row in warehouse.split("\n")], "".join(movement.split("\n"))

def adjust_warehouse(warehouse):
  char_map = {".": "..", "O": "[]", "#": "##", "@": "@."}
  return [list("".join([char_map[char] for char in row])) for row in warehouse]

def create_map(warehouse):
  return {
    complex(i, j): char
    for i, row in enumerate(warehouse)
    for j, char in enumerate(row)
  }

def create_map_part_two(new_warehouse):
  walls, boxes = set(), {}
  start = None
  for i, row in enumerate(new_warehouse):
    for j, char in enumerate(row):
      if char == "#":
        walls.add(complex(i, j))
      elif char == "[":
        boxes[complex(i, j)] = complex(i, j + 1)
        boxes[complex(i, j + 1)] = complex(i, j)
      elif char == "@":
        start = complex(i, j)
  return walls, boxes, start

def find_start(warehouse_map):
  return next(pos for pos in warehouse_map if warehouse_map[pos] == "@")

def find_empty_space(warehouse_map, offset, pos):
  while warehouse_map[pos] != "#":
    if warehouse_map[pos] == ".":
      return pos
    pos += offset
  return None

def bfs(new_pos, boxes, offset):
  visited = set()
  queue = deque([new_pos])
  while queue:
    current = queue.popleft()
    if current in visited:
      continue
    visited.add(current)
    queue.append(boxes[current])
    if current + offset in boxes:
      queue.append(current + offset)
  return visited

def first_part(warehouse_map, movement, start):
  pos = start
  for step in movement:
    offset = DIRECTIONS[step]
    empty_space = find_empty_space(warehouse_map, offset, pos)
    if not empty_space:
      continue
    while empty_space != pos:
      prev = empty_space - offset
      warehouse_map[empty_space], warehouse_map[prev] = (
        warehouse_map[prev],
        warehouse_map[empty_space],
      )
      empty_space = prev
    pos += offset
  return sum(
    100 * pos.real + pos.imag for pos in warehouse_map if warehouse_map[pos] == "O"
  )

def second_part(walls, boxes, start, movement):
  pos = start
  for step in movement:
    offset = DIRECTIONS[step]
    new_pos = pos + offset
    if new_pos in walls:
      continue
    if new_pos not in boxes:
      pos = new_pos
    else:
      cluster = bfs(new_pos, boxes, offset)
      cluster_dict = {key + offset: value + offset for key, value in boxes.items() if key in cluster}
      if not cluster_dict.keys() & walls:
        boxes = {key: value for key, value in boxes.items() if key not in cluster} | cluster_dict
        pos = new_pos

  return sum(50 * box.real + box.imag / 2 - 0.25 for box in boxes)

if __name__ == "__main__":
  warehouse, movement = read_input()
  warehouse_map = create_map(warehouse)
  start = find_start(warehouse_map)
  print("First part result:", first_part(warehouse_map, movement, start))

  new_warehouse = adjust_warehouse(warehouse)
  walls, boxes, start = create_map_part_two(new_warehouse)
  print("Second part result:", second_part(walls, boxes, start, movement))