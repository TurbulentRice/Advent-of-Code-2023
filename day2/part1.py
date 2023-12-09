import re

with open('input.txt', 'r') as file:
  lines = file.readlines()
  game_id_sum = 0
  for line in lines:
    line = line.strip()

    # Game ID
    game_id = int(re.findall('\d+', line[:line.index(':')])[0])

    # Game rounds
    game_rounds = [game_round.strip().split(", ") for game_round in line[line.index(":") + 2:].split(";")]

    # Format the data so we can analyze it easer
    game_data = []
    pattern = re.compile(r'\b(?:\w+|\d)\b')
    for index, round in enumerate(game_rounds):
      game_data.append({})
      for result in round:
        result_data = pattern.findall(result)
        game_data[index][result_data[1]] = int(result_data[0])
    
    max_reds = max([round.get('red', 0) for round in game_data])
    max_greens = max([round.get('green', 0) for round in game_data])
    max_blues = max([round.get('blue', 0) for round in game_data])

    # Elf wants to know if this game would be possible if the bag contained ONLY:
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    if max_reds <= 12 and max_greens <= 13 and max_blues <= 14:
      game_id_sum += game_id

print(f"Game ID sum: {game_id_sum}")
