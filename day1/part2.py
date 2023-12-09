import re

numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
total = 0

with open('input.txt', 'r') as file:
  lines = file.readlines()

  for line in lines:
    print("Line: " + line.strip())

    # Match single digits and substrings from numbers
    pattern = re.compile(f"(?=(\d|{'|'.join(map(re.escape, numbers.keys()))}))")
    number_list = pattern.findall(line)

    # Convert the words to their numeric form
    number_list = [numbers.get(number_string, number_string) for number_string in number_list]

    value = int(f"{number_list[0]}{number_list[-1]}")
    print(f"Value: {value}")

    total += value

print(f"Total: {total}")
