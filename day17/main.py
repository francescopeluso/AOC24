#
#   Advent of Code 2024 - Day 17
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#


def read_input():
  with open('input.txt') as f:
    lines = f.read().splitlines()
    reg_a = int(lines[0].split(': ')[1])
    reg_b = int(lines[1].split(': ')[1])
    reg_c = int(lines[2].split(': ')[1])
    program = [int(x) for x in lines[4].split(': ')[1].split(',')]

    return reg_a, reg_b, reg_c, program


def eval_program(a, b, c, program):
  i = 0
  outputs = []
  
  while i in range(len(program)-1):
    combo = {0:0, 1:1, 2:2, 3:3, 4:a, 5:b, 6:c}
    
    op, val = program[i:i+2]
    
    match op:
      case 0: a = a >> combo[val]               # adv
      case 1: b = b ^ val                       # bxl
      case 2: b = combo[val] & 7                # bst
      case 3: i = val-2 if a else i             # jnz
      case 4: b = b ^ c                         # bxc
      case 5: outputs.append(combo[val] & 7)    # out
      case 6: b = a >> combo[val]               # bdv
      case 7: c = a >> combo[val]               # cdv
        
    i += 2
      
  return outputs


def find_recursive(a, i, program):
  result = eval_program(a, 0, 0, program)
  if result == program:
    return a
      
  if not i or result == program[-i:]:
    for n in range(8):
      found = find_recursive(8*a + n, i+1, program)
      if found is not None:
        return found
  
  return None


def first_part():
  reg_a, reg_b, reg_c, program = read_input()
  result = eval_program(reg_a, reg_b, reg_c, program)
  return ','.join(map(str, result))


def second_part():
  _, _, _, program = read_input()
  return find_recursive(0, 0, program)


if __name__ == "__main__":
  print("First part:", first_part())
  print("Second part:", second_part())