#
#   Advent of Code 2024 - Day 3
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

import re

def read_input():
  with open("input.txt") as f:
    return f.read()


def product_sum(matches):
  product_sum = 0

  for match in matches:
    pair = match[4:-1].split(',')
    if len(pair[0]) < 4 and len(pair[1]) < 4:
      product_sum += int(pair[0]) * int(pair[1])

  return product_sum


def first_part(instruction):

  mul_pattern = r"mul\(\d+,\s*\d+\)"
  matches = re.findall(mul_pattern, instruction)

  return product_sum(matches)


def second_part(instruction):

  mul_do_dont_pattern = r"mul\(\d+,\s*\d+\)|do\(\)|don't\(\)"
  matches = re.findall(mul_do_dont_pattern, instruction)

  do_include = True
  to_do = []
  
  for match in matches:
    if match == "do()":
      do_include = True
    elif match == "don't()":
      do_include = False
    else:
      if do_include:
        to_do.append(match)

  return product_sum(to_do)


if __name__ == "__main__":
  instruction = read_input()

  print("First part result: " + str(first_part(instruction)))
  print("Second part result: " + str(second_part(instruction)))