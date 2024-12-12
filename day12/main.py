#
#   Advent of Code 2024 - Day 12
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

from collections import deque

alternatives = [(-1, 0), (0, -1), (1, 0), (0, 1)]
direction = { "^": ((0, -1), (0, 1)), ">": ((1, 0), (-1, 0)), "v": ((0, 1), (0, -1)), "<": ((-1, 0), (1, 0))}

sym = { (-1, 0): '^', (0, -1): '<', (1, 0): 'v', (0, 1): '>' }

def read_input():
  try:
    with open('input.txt', 'r') as file:
      return [line.strip() for line in file]
  except FileNotFoundError:
    print("Input file not found!")
    return []
  

def invalid(x, y, mat):
  return not (x >= 0 and x < len(mat) and y >= 0 and y < len(mat[x]))


def walkBorder(e):
  s = 0
  for k in e:

    x = e[k]
    a, b = direction[k]

    while len(x) > 0:
      p = x.pop()

      k = (p[0] + a[0], p[1] + a[1])

      while k in x:
        x.remove(k)
        k = (k[0] + a[0], k[1] + a[1])

      k = (p[0] + b[0], p[1] + b[1])

      while k in x:
        x.remove(k)
        k = (k[0] + b[0], k[1] + b[1])

      s += 1

  return s

def flood(mat, start, visit):
    
  v = mat[start[0]][start[1]]
  a = 0
  p = 0
  e = {}

  for k in sym.values():
    e[k] = set()

  q = deque([start])

  while q:

    d = q.popleft()
    if d in visit:
      continue

    visit.add(d)
    a += 1

    for u in alternatives:
      x = d[0] + u[0]
      y = d[1] + u[1]

      if invalid(x, y, mat):
        p += 1
        e[sym[u]].add(d)

      elif mat[x][y] != v:
        p += 1
        e[sym[u]].add(d)

      else:
        q.append((x, y))

  return a, p, e


def first_part(garden_map):
  rows, cols = len(garden_map), len(garden_map[0])
  visited = set()
  total_price = 0

  for r in range(rows):
    for c in range(cols):
      if (r, c) not in visited:
        area, perimeter, _ = flood(garden_map, (r, c), visited)
        total_price += area * perimeter

  return total_price


def second_part(garden_map):
  rows, cols = len(garden_map), len(garden_map[0])
  visited = set()
  total_price = 0

  for r in range(rows):
    for c in range(cols):
      if (r, c) not in visited:
        v = garden_map[r][c]
        area, _, external = flood(garden_map, (r, c), visited)
        s = walkBorder(external)
        total_price += area * s

  return total_price


if __name__ == "__main__":
    input_map = read_input()

    print("First part result:", first_part(input_map))
    print("Second part result:", second_part(input_map))