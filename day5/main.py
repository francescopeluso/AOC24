#
#   Advent of Code 2024 - Day 5
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

def read_input():
  rules, updates = [], []

  with open("input.txt") as f:
    text = f.read().split("\n\n")
    entries = text[0].split("\n")

    for row in entries:
      rules.append(list(map(int, row.split("|"))));

    orders = text[1].split("\n")
    for row in orders:
      updates.append(list(map(int, row.split(","))))

  return rules, updates


def parse_rules_to_dict(rules):
  rule_dict = {}
  for rule in rules:
    a, b = map(int, rule)
    if a not in rule_dict:
      rule_dict[a] = set()
    rule_dict[a].add(b)

  return rule_dict


def is_ordered(update, rule_dict):
  page_index = {page: i for i, page in enumerate(update)}
  for a, dependencies in rule_dict.items():
    if a not in page_index: # page not in update, so we don't check it
      continue
    for b in dependencies:
      if b in page_index and page_index[a] > page_index[b]:
        return False  # rule was not followed
      
  return True


def sort_pages(update, rule_dict):
  n = len(update)
  sorted_update = update[:]
  
  # Keep sorting until no changes are made
  for _ in range(n):
    swapped = False
    for i in range(n - 1):
      a = sorted_update[i]
      b = sorted_update[i + 1]
      
      if a in rule_dict and b in rule_dict[a]:
        sorted_update[i], sorted_update[i + 1] = sorted_update[i + 1], sorted_update[i]
        swapped = True

    if not swapped:
      break

  return sorted_update


def first_part(rules, updates):

  rule_dict = parse_rules_to_dict(rules)
  middle_pages = []

  for update in updates:
    if is_ordered(update, rule_dict):
      middle_index = len(update) // 2
      middle_pages.append(update[middle_index])

  print(middle_pages)
  return sum(middle_pages)


def second_part():
  
  rule_dict = parse_rules_to_dict(rules)
  middle_pages = []

  for update in updates:
    if not is_ordered(update, rule_dict):
      ordered_update = sort_pages(update, rule_dict)
      middle_index = len(ordered_update) // 2 
      middle_pages.append(ordered_update[middle_index])

  return sum(middle_pages)

if __name__ == "__main__":
  rules, updates = read_input()

  print("First part result: " + str(first_part(rules, updates)))
  print("Second part result: " + str(second_part()))
  print()