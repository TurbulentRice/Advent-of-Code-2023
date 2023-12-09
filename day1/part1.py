total = 0

with open('input.txt', 'r') as file:
  lines = file.readlines()
  
  first_number = "0"
  last_number = "0"

  for line in lines:
    line = line.strip()
    print("Line: " + line)

    # Iterate forward until the first numeric character is found
    for char_index, char in enumerate(line):
      if char.isdigit():
        first_number = char
        break

    # Iterate backward until the first numeric character is found
    for char_index in range(len(line) - 1, -1, -1):
      char = line[char_index]
      if char.isdigit():
        last_number = char
        break

    value = int(f"{first_number}{last_number}")
    print(f"Value: {value}")
    total += value
    
print(f"Total: {total}")
