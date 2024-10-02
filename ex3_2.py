# Define the set of valid numeric characters
numbers = set('1234567890')
numbers_with_location = []
partial_numbers = ''
numbers_scheme = []
symbol_location = []
checks = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
total_sum = 0

# Read the engine schematic from the file
with open('ex3.txt', 'r') as f:
    lines = f.readlines()

# Make the matrix
matrix = []
for row in lines:
    matrix.append(row.strip())

# Detect numbers and their locations
for c in range(len(matrix)):
    for r in range(len(matrix[c])):
        if matrix[c][r] in numbers:
            partial_numbers += matrix[c][r]
            numbers_scheme.append((c, r))
        else:
            if partial_numbers != '':
                numbers_with_location.append({partial_numbers: numbers_scheme})
                partial_numbers = ''
                numbers_scheme = []
    if partial_numbers != '':
        numbers_with_location.append({partial_numbers: numbers_scheme})
        partial_numbers = ''
        numbers_scheme = []

# Detect the locations of the * symbol
for c in range(len(matrix)):
    for r in range(len(matrix[c])):
        if matrix[c][r] == "*":
            symbol_location.append((c, r))

# Calculate the sum of all gear ratios
for symbol in symbol_location:
    adjacents = set()  # Use a set to avoid duplicate entries
    for check in checks:
        location_checker = (symbol[0] + check[0], symbol[1] + check[1])
        
        # Check if the calculated neighbor is within bounds and is a number
        if (0 <= location_checker[0] < len(matrix) and 
            0 <= location_checker[1] < len(matrix[0]) and 
            matrix[location_checker[0]][location_checker[1]] in numbers):
            
            # Find the corresponding number for this location
            for number_entry in numbers_with_location:
                for number, location in number_entry.items():
                    # Check if location_checker is in the list of locations
                    if location_checker in location:
                        adjacents.add(int(number))  # Collect the number in a set

    # If exactly two adjacent numbers are found, calculate the product
    if len(adjacents) == 2:
        adjacents_list = list(adjacents)
        product = adjacents_list[0] * adjacents_list[1]
        total_sum += product
        print(f"Gear at {symbol}: {adjacents_list[0]} * {adjacents_list[1]} = {product}")

print("Total Sum of all gear ratios:", total_sum)

