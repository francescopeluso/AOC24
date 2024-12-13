#
#   Advent of Code 2024 - Day 13
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

def is_close_to_integer(num):
  return abs(round(num) - num) < 0.001


def read_input():
  with open('input.txt', 'r') as f:
    input_data = f.read()

  lines = input_data.split('\n')
  problems = [[]]
  
  for line in lines:
    line = line.strip()
    if line == '':
      problems.append([])
      continue

    parts = line.split(':')
    identifier = parts[0][0]
    parts = parts[1].split(',')
    
    if identifier == 'B':
      num1 = int(parts[0].split('+')[1])
      num2 = int(parts[1].split('+')[1])
    else:
      num1 = int(parts[0].split('=')[1])
      num2 = int(parts[1].split('=')[1])
    
    problems[-1].append(num1)
    problems[-1].append(num2)
  
  return problems


def solve_claw_machine(problems, part2=False):
  total = 0
  
  for problem in problems:
    ax = problem[0]
    ay = problem[1]
    bx = problem[2]
    by = problem[3]
    gx = problem[4]
    gy = problem[5]
    
    if part2:
      gx += 10_000_000_000_000
      gy += 10_000_000_000_000
    
    slope_a = ay / ax
    y_intecept_a = gy - slope_a * gx

    slope_b = by / bx
    y_intercept_b = 0

    x_intersection = (y_intercept_b - y_intecept_a) / (slope_a - slope_b)

    b_count = x_intersection / bx
    a_count = (gx - x_intersection) / ax
    
    solved = is_close_to_integer(a_count) and is_close_to_integer(b_count)
    if solved:
      a_count = round(a_count)
      b_count = round(b_count)
      total += a_count * 3 + b_count
  
  return total


def first_part(problems):
  return solve_claw_machine(problems)


def second_part(problems):
  return solve_claw_machine(problems, part2=True)


if __name__ == "__main__":
  machines = read_input()
  
  print("First part result:", first_part(machines))
  print("Second part result:", second_part(machines))