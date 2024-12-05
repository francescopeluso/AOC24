#
#   Advent of Code 2024 - Day 4
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

import re

def read_input():
  matrix = []

  with open("input.txt") as f:
    for line in f:
      matrix.append(line.strip())
  
  return matrix


def print_matrix(matrix):
  for row in matrix:
    print(''.join([char for char in row]))


def get_diagonals():
  diagonals = []
  rows, cols = len(matrix), len(matrix[0])

  # top-left to bottom-right
  for d in range(-(rows - 1), cols):
      diag = [matrix[i][i - d] for i in range(max(0, d), min(rows, cols + d))]
      diagonals.append(diag)

  # top-right to bottom-left
  for d in range(rows + cols - 1):
      diag = [matrix[i][d - i] for i in range(max(0, d - cols + 1), min(rows, d + 1))]
      diagonals.append(diag)

  return diagonals


def count_with_pattern(matrix, pattern):
    occurrences = 0
    for row in matrix:
        row_str = ''.join(row)
        occurrences += len(re.findall(pattern, row_str))
        occurrences += len(re.findall(pattern, row_str[::-1]))  # check for matches on reversed string
    return occurrences


def check_x_mas(matrix, i, j):
  rows, cols = len(matrix), len(matrix[0])

  if i - 1 < 0 or i + 1 >= rows or j - 1 < 0 or j + 1 >= cols:
      return False

  patterns = ["MAS", "SAM"]

  l_diag = ''.join([matrix[i - 1][j - 1], matrix[i][j], matrix[i + 1][j + 1]])
  r_diag = ''.join([matrix[i - 1][j + 1], matrix[i][j], matrix[i + 1][j - 1]])

  if (l_diag in patterns and r_diag in patterns) or (l_diag[::-1] in patterns and r_diag[::-1] in patterns):
    return True

  return False


def first_part(matrix):
  pattern = r'XMAS'

  occurrences = count_with_pattern(matrix, pattern)
  occurrences += count_with_pattern(list(zip(*matrix)), pattern)  # checking for vertical occurrences too
  occurrences += count_with_pattern(get_diagonals(), pattern)

  return occurrences


def second_part(matrix):
  rows, cols = len(matrix), len(matrix[0])
  count = 0

  for i in range(1, rows - 1):
    for j in range(1, cols - 1):
      if check_x_mas(matrix, i, j):
        count += 1

  return count

if __name__ == "__main__":
  matrix = read_input()

  print("First part result: " + str(first_part(matrix)))
  print("Second part result: " + str(second_part(matrix)))
  print()