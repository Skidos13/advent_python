games_list = []
games_dict = {}
game_number_sum=0
game_standard={'red':12 , 'blue':14, 'green':13}
with open('ex2.txt', 'r') as f:
    games = f.readlines()

# Process each game and create a dictionary of game number to colors
for game in games:
    games_list.append(game.strip().split(':'))

for x in range(len(games_list)):
    # Split colors and counts for each game
    value = games_list[x][1].replace(';', ',').split(',')
    
    # Initialize a color count for the current game
    color_counts = {'red': 0, 'blue': 0, 'green': 0}
    
    # Count colors for the current game
    for color_info in value:
        count_color = color_info.strip().split()  # Split on whitespace
        if len(count_color) == 2:  # Ensure we have both count and color
            count = int(count_color[0])  # The count (first element)
            color = count_color[1]  # The color (second element)
            color_counts[color] += count
    
    # Create a unique representation for the game's color counts
    unique_colors = ", ".join(f"{color_counts[color]} {color}" for color in color_counts if color_counts[color] > 0)
    
    # Update the dictionary with the unique colors
    games_dict[x + 1] = unique_colors

for key,values in games_dict.items():
    # Transform the string to a list
    values_list = values.split(', ')
    
    # Make values a dictionary with the color and the count
    values_dict = {}
    for item in values_list:
        count, color = item.split()
        values_dict[color] = int(count)

    #update the values of the dictionary
    games_dict[key] = values_dict


for key,values in games_dict.items():
    print(key,values)

for key,values in games_dict.items():
    #if the game value is the same  or lower than the standard game values add the game number to the sum
    if values['red'] <= game_standard['red'] and values['blue'] <= game_standard['blue'] and values['green'] <= game_standard['green']:
       print(key)
       print(games_dict[key])
       game_number_sum += key