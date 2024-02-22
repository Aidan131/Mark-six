import itertools

numbers = list(range(1, 50))  # Generate a list of numbers from 1 to 49
combinations = list(itertools.combinations(numbers, 6))  # Generate all combinations of 6 numbers

# Print all combinations
with open('./possibility.txt', 'w') as f:
    for combination in combinations:
        f.write(' '.join(map(str, combination)) + '\n')
        
f.close