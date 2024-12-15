#
#   Advent of Code 2024 - Day 13
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

def read_input():
  with open('input.txt', 'r') as f:
      return f.readlines()


def parse_robots(input_data):
  robots = []
  for line in input_data:
    line = line.strip().split()
    pos = tuple(int(n) for n in line[0].split('=')[1].split(','))
    vel = tuple(int(n) for n in line[1].split('=')[1].split(','))
    robots.append((pos, vel))
  return robots


def calc_position(robot, seconds):
  (x, y), (dx, dy) = robot
  return ((x + seconds * dx) % 101, (y + seconds * dy) % 103)


def calculate_safety(robots, seconds):
  q1 = q2 = q3 = q4 = 0
  for robot in robots:
    x, y = calc_position(robot, seconds)
    if x < 50:
      if y < 51:
        q1 += 1
      elif y > 51:
        q2 += 1
    elif x > 50:
      if y < 51:
        q3 += 1
      elif y > 51:
        q4 += 1
  return q1 * q2 * q3 * q4


def display_grid(robots, seconds):
  layout = [['.'] * 101 for _ in range(103)]
  for robot in robots:
    x, y = calc_position(robot, seconds)
    layout[y][x] = 'X'
  for row in layout:
    print(''.join(row))


def first_part(input_data):
  robots = parse_robots(input_data)
  return calculate_safety(robots, 100)


def second_part(input_data):
  robots = parse_robots(input_data)
  safety = [calculate_safety(robots, sec) for sec in range(101*103)]
  
  for sec, _ in sorted(enumerate(safety), key=lambda x: x[1]):
    print(f"\nChecking time: {sec} seconds")
    display_grid(robots, sec)
    return sec
  
  return None


if __name__ == "__main__":
    input_data = read_input()
    print("First part result:", first_part(input_data))
    print("Second part result:", second_part(input_data))