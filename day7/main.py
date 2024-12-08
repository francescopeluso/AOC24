#
#   Advent of Code 2024 - Day 7
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

def read_input():
  expected_results, operands = [], []

  with open("input.txt") as f:
    for row in f:
      if not row.strip():
        continue
      sections = row.split(":")
      expected_results.append(int(sections[0].strip()))
      operands.append(sections[1].strip().split(" "))

  return expected_results, operands


def eval_ltr(expr):
  expr = expr.split(" ")
  result = int(expr[0])

  for i in range(1, len(expr), 2):
    operator = expr[i]
    next_val = int(expr[i + 1])
    if operator == "+":
      result += next_val
    elif operator == "*":
      result *= next_val
    elif operator == "||":
      result = int(str(result) + str(next_val))
    
  return result


def generate_combos_recursive(operators, ops, idx, current):
  if idx == len(ops) - 1:
    yield current
  else:
    for op in operators:
      yield from generate_combos_recursive(operators, ops, idx + 1, current + f" {op} {ops[idx + 1]}")


def validate_and_sum(er, ops, operators):
  verified = {}

  for target, operand_list in zip(er, ops):
    # Generate combinations using recursion
    for combo in generate_combos_recursive(operators, operand_list, 0, operand_list[0]):
      try:
        if eval_ltr(combo) == target and ''.join(operand_list) not in verified:
          verified[''.join(operand_list)] = target
      except ValueError:
        continue

  return sum(verified.values())


def first_part(er, ops):
  operators = ["+", "*"]
  return validate_and_sum(er, ops, operators)


def second_part(er, ops):
  operators = ["+", "*", "||"]
  return validate_and_sum(er, ops, operators)


if __name__ == "__main__":
  er, ops = read_input()

  print("First part result: " + str(first_part(er, ops)))
  print("Second part result: " + str(second_part(er, ops)))
  print()
