#
#   Advent of Code 2024 - Day 11
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

from functools import cache

def read_input():
  with open('input.txt', 'r') as f:
    return list(map(int, f.read().split()))

@cache
def count_stones(stone, it):
  if it == 0:
    return 1
  if stone == 0:
    return count_stones(1, it-1)
  
  s = str(stone)
  l = len(s)
  if l % 2 == 1:
    return count_stones(stone * 2024, it-1)

  return count_stones(int(s[: l // 2]), it-1) + count_stones(int(s[l // 2:]), it-1)          

def first_part(stones):
  return sum(map(lambda s: count_stones(s, 25), stones))

def second_part(stones):
  return sum(map(lambda s: count_stones(s, 75), stones))

if __name__ == "__main__":
  stones = read_input()
  print("First part result:", first_part(stones))
  print("Second part result:", second_part(stones))
