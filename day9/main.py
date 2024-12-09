#
#   Advent of Code 2024 - Day 9
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

def read_input():
  with open('input.txt', 'r') as file:
    return file.readline().strip()
  

def get_formatted_disk(line):
  blocks = []
  empty, inc_id = False, 0

  for ch in line:
    if not empty:
      blocks.append([str(inc_id)] * int(ch))
      inc_id += 1
    else:
      blocks.append(['.'] * int(ch))

    empty = not empty

  disk = []
  for block in blocks:
    disk += block

  return disk


def fill_spaces(disk):
  l, r = 0, len(disk) - 1

  while True:
    moved = False

    while l < r:
      while l < r and disk[l] != '.':
        l += 1
      while l < r and disk[r] == '.':
        r -= 1
        moved = True
      
      if l < r:
        disk = disk[:l] + [disk[r]] + disk[l+1:r] + [disk[l]] + disk[r+1:]
        l += 1
        r -= 1

    if not moved:
      break

  return disk


def calculate_checksum(disk):
  checksum = 0
  for i in range(len(disk)):
    if disk[i].isdigit():
      checksum += int(disk[i]) * i
  return checksum


def get_file_positions(disk):
  files = []
  i = 0

  while i < len(disk):
    if disk[i].isdigit():
      start = i
      current_id = disk[i]
      while i < len(disk) and disk[i].isdigit() and disk[i] == current_id:
        i += 1
      files.append((start, i - 1))
    else:
      i += 1

  return files


def move_files(disk, files):

  # why not?
  def find_free_space(disk, start, length):
    i = 0
    while i < start:
      if disk[i] == '.':
        space_count = 0
        j = i
        while j < len(disk) and disk[j] == '.' and space_count < length:
          space_count += 1
          j += 1
        if space_count >= length:
          return i
      i += 1
    return -1

  sorted_files = sorted(files, key=lambda x: int(disk[x[0]]), reverse=True)

  for start, end in sorted_files:
    file_length = end - start + 1
    file_id = disk[start]
    
    new_pos = find_free_space(disk, start, file_length)
    
    if new_pos != -1:
      file_content = [file_id] * file_length
      disk[start:end + 1] = ['.'] * file_length
      disk[new_pos:new_pos + file_length] = file_content


def first_part(line):
  disk = get_formatted_disk(line)
  defragmented_disk = fill_spaces(disk)
  return calculate_checksum(defragmented_disk)
  

def second_part(line):
  disk = get_formatted_disk(line)
  files = get_file_positions(disk)
  move_files(disk, files)
  return calculate_checksum(disk)


if __name__ == "__main__":
  line = read_input()

  print("First part result: " + str(first_part(line)))
  print("Second part result: " + str(second_part(line)))
  print()