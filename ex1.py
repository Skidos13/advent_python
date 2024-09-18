with open("ex1_values.txt") as file:
    lines = file.readlines()

sum = 0  # Initialize sum

for line in lines:
    line_list = list(line)

    first_number = None
    last_number = None
    
    # Find the first number in the line
    for char in line_list:
        if char.isdigit():
            first_number = char
            break
    
    # Find the last number in the line
    for char in reversed(line_list):
        if char.isdigit():
            last_number = char
            break

    # Ensure both numbers are found before combining
    if first_number is not None and last_number is not None:
        combined_number = int(first_number + last_number)
        sum += combined_number

print(sum)