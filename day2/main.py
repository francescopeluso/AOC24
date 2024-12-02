#
#   Advent of Code 2024 - Day 2
#   Francesco Peluso - @francescopeluso on GitHub
#   Repo:         https://github.com/francescopeluso/AOC24
#   My website:   https://francescopeluso.xyz
#

def read_input():
  reports = []

  with open("input.txt") as f:
    for line in f:
      reports.append([int(char) for char in line.strip().split(" ")])
  
  return reports


def is_safe(report):
  i, safe = 1, True
  while i < len(report) and safe:
    if abs(report[i] - report[i-1]) > 3 or report[i] == report[i-1]:
      safe = False
    i += 1
  return safe

def remove_out_of_order(report):
  for i in range(1, len(report)):
      if report[i] < report[i - 1]:
          return report[:i] + report[i+1:] 
  return report

def try_fix(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report) and (modified_report == sorted(modified_report) or modified_report == sorted(modified_report, reverse=True)):
            return modified_report
        
    return report


def first_part(reports):
  safe_reports = 0
  for report in reports:
    if report == sorted(report) or report == sorted(report, reverse=True):
      if is_safe(report):
        safe_reports += 1

  return safe_reports


def second_part(reports, safe):
  actually_safe_reports = safe

  for report in reports:
      if not is_safe(report) or (report != sorted(report) and report != sorted(report, reverse=True)):
          fixed_report = try_fix(report) 
          if is_safe(fixed_report) and (fixed_report == sorted(fixed_report) or fixed_report == sorted(fixed_report, reverse=True)):
              actually_safe_reports += 1

  return actually_safe_reports


if __name__ == "__main__":
  reports = read_input()

  safe = first_part(reports)
  actually_safe = second_part(reports, safe)

  print("First part result: " + str(safe))
  print("Second part result: " + str(actually_safe))