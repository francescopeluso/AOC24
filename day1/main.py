#
#   Advent of Code 2024 - Day 1
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

def read_input():
  left, right = [], []
  with open("input.txt") as f:
    for line in f:
      values = line.split("   ");
      left.append(int(values[0]))
      right.append(int(values[1]))

  left.sort()
  right.sort()

  return left, right


def first_part(left, right):
  distances_sum = 0
  for i in range(len(left)):
    distances_sum += abs(left[i] - right[i])

  return abs(distances_sum)


def second_part(left, right):
  product_sum = 0
  for l_value in left:
    product_sum += l_value * right.count(l_value)

  return product_sum


if __name__ == "__main__":
  left, right = read_input();
  print("First part result: " + str(first_part(left, right)))
  print("Second part result: " + str(second_part(left, right)))