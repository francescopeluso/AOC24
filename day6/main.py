#
#   Advent of Code 2024 - Day 6
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

def read_input():
  matrix = []
  guard_x, guard_y = 0, 0

  with open("input.txt") as f:
    text = f.read().split("\n")
    for row in text:
      matrix.append(list(row))
      if "^" in row:
        guard_x, guard_y = row.index('^'), len(matrix) - 1

  return matrix, guard_x, guard_y


def print_matrix(matrix):
  for row in matrix:
    print("".join(row))


def simulate_guard(matrix, start_x, start_y, obstruction=None):
  directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
  actual_direction = 0
  x, y = start_x, start_y
  visited = set()

  if obstruction:
    matrix[obstruction[1]][obstruction[0]] = 'O'

  while True:
    if (x, y, actual_direction) in visited:
        return True
    
    visited.add((x, y, actual_direction))

    next_x, next_y = x + directions[actual_direction][0], y + directions[actual_direction][1]

    if next_y < 0 or next_y >= len(matrix) or next_x < 0 or next_x >= len(matrix[0]) or matrix[next_y][next_x] in ['#', 'O']:
      actual_direction = (actual_direction + 1) % 4
    else:
      x, y = next_x, next_y

    if next_y < 0 or next_y >= len(matrix) or next_x < 0 or next_x >= len(matrix[0]):
      break

  return False


def first_part(matrix, start_x, start_y):
  directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
  actual_direction = 0

  x, y = start_x, start_y

  steps = 0

  while True:
    try:
      if matrix[y + directions[actual_direction][1]][x+directions[actual_direction][0]] == '#': # obstacle detected
        actual_direction = (actual_direction + 1) % 4
      else:
        matrix[y][x] = 'X'
        x += directions[actual_direction][0]
        y += directions[actual_direction][1]
        steps += 1 if matrix[y][x] != 'X' else 0
    except IndexError:
      steps += 1
      return steps


def second_part(matrix, start_x, start_y):
  loop_positions = 0
  rows, cols = len(matrix), len(matrix[0])

  for y in range(rows):
    for x in range(cols):
      if matrix[y][x] == '#' or (x, y) == (start_x, start_y):
        continue

      if simulate_guard([row[:] for row in matrix], start_x, start_y, (x, y)):
        loop_positions += 1

  return loop_positions


if __name__ == "__main__":
  matrix, start_x, start_y = read_input()

  matrix[start_y][start_x] = '.'
  print("First part result: " + str(first_part(matrix, start_x, start_y)))
  print("Second part result: " + str(second_part(matrix, start_x, start_y)))
  print()