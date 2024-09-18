digit_map = {
    'one': '1', 'two': '2', 'three': '3',
    'four': '4', 'five': '5', 'six': '6', 'seven': '7',
    'eight': '8', 'nine': '9'}

total_sum = 0

with open("ex1_values.txt") as file:
    lines = file.readlines()

# Function to replace spelled-out digits with numeric digits
def replace_spelled_digits(line):
    for word, digit in digit_map.items():
        line = line.replace(word, digit)  # Replace spelled-out digits with numbers
    return line

# Process each line and replace spelled-out digits
updated_lines = [replace_spelled_digits(line) for line in lines]

for string in updated_lines:
    print(string)
    line_list = list(string)

    first_number = None
    last_number = None
    
    # Find the first number in the line
    for char in line_list:
        if char.isdigit():
            first_number = str(char)
            break
    
    # Find the last number in the line
    for char in reversed(line_list):
        if char.isdigit():
            last_number = str(char)
            break
    print(first_number, last_number)
    # Ensure both numbers are found before combining
    if first_number is not None and last_number is not None:
        combined_number = int(first_number + last_number)
        print (combined_number)
        total_sum += combined_number

print("total sum:",total_sum)