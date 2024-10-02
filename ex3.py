matrix = []
numbers = set('1234567890')
numbers_scheme = []
partial_numbers = ''
numbers_with_location = []
sum_parts = 0  # Renamed to avoid shadowing built-in `sum`

with open('ex3.txt', 'r') as f:
    puzzle = f.readlines()

for row in puzzle:
    matrix.append(row.strip())

for c in range(len(matrix)):
    for r in range(len(matrix[c])):
        if matrix[c][r] in numbers:
            partial_numbers += matrix[c][r]
            numbers_scheme.append((c, r))
        else:
            if partial_numbers != '':
                numbers_with_location.append((partial_numbers, numbers_scheme))
                partial_numbers = ''
                numbers_scheme = []
    # Handle the case where a number ends at the end of a row
    if partial_numbers != '':
        numbers_with_location.append((partial_numbers, numbers_scheme))
        partial_numbers = ''
        numbers_scheme = []

# Check adjacent symbols
checks = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

for number, locations in numbers_with_location:
    adjacent = False
    for location in locations:
        for check in checks:
            checked_location = (location[0] + check[0], location[1] + check[1])
            # If checked location is in the matrix and is different than '.' and not a number, then it is adjacent
            if 0 <= checked_location[0] < len(matrix) and 0 <= checked_location[1] < len(matrix[0]) and matrix[checked_location[0]][checked_location[1]] != '.' and matrix[checked_location[0]][checked_location[1]] not in numbers:
                adjacent = True
                break
        if adjacent:
            break

    if adjacent:
        sum_parts += int(number)

print(sum_parts)
