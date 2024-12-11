#
#   Advent of Code 2024 - Day 10
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#


def read_input():
  with open('input.txt', 'r') as file:
    return [num for num in file.readline().strip().split(" ")]


def rearrange_stones(stones):
  new_stones = []

  for stone in stones:

    if stone == "0":
      new_stones.append("1")

    elif len(stone) % 2 == 0:
      half_len = len(stone) // 2
      left_stone = str(int(stone[:half_len]))
      right_stone = str(int(stone[half_len:]))
      new_stones.append(left_stone)
      new_stones.append(right_stone)

    else:
      new_stones.append(str(int(stone) * 2024))

  return new_stones


def first_part(stones):
  current_stones = stones.copy()

  for _ in range(25):
    current_stones = rearrange_stones(current_stones)

  return len(current_stones)


def second_part(stones):
  current_stones = stones.copy()

  for _ in range(75):
    current_stones = rearrange_stones(current_stones)
    print("Actual length:", _, len(current_stones))

  return len(current_stones)

if __name__ == "__main__":
  stones = read_input()
    
  print("First part result:", first_part(stones))
  print("Second part result:", second_part(stones))