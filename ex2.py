total_power = 0

with open('ex2.txt', 'r') as f:
    games = f.readlines()

for game in games:
    game_id, rounds = game.strip().split(':')
    rounds = rounds.split(';')

    # Initialize the minimum counts for each color
    min_cubes = {'red': 0, 'blue': 0, 'green': 0}

    for round in rounds:
        color_counts = {'red': 0, 'blue': 0, 'green': 0}
        cubes = round.split(',')
        for cube in cubes:
            count, color = cube.strip().split()
            color_counts[color] += int(count)

        # Update the minimum counts with the maximum seen so far
        for color in color_counts:
            if color_counts[color] > min_cubes[color]:
                min_cubes[color] = color_counts[color]

    # Calculate the power of the minimum set of cubes
    power = min_cubes['red'] * min_cubes['blue'] * min_cubes['green']
    total_power += power

print(total_power)
