# Define the vectors
vectors = {
    'r': [-1, -2],
    's': [-3, 3],
    'u': [2, -1],
    'v': [3, 1],
    'w': [1, 3]
}

# Function to calculate the dot product of two vectors
def dot_product(vector1, vector2):
    result = sum(x * y for x, y in zip(vector1, vector2))
    return result

# Get user input for the first vector
vector_name1 = input('Enter the first vector (r, s, u, v, w): ')
while vector_name1 not in vectors:
    print('Invalid vector name. Please choose from r, s, u, v, or w.')
    vector_name1 = input('Enter the first vector (r, s, u, v, w): ')

# Get user input for the second vector
vector_name2 = input('Enter the second vector (r, s, u, v, w): ')
while vector_name2 not in vectors:
    print('Invalid vector name. Please choose from r, s, u, v, or w.')
    vector_name2 = input('Enter the second vector (r, s, u, v, w): ')

# Calculate the dot product
result = dot_product(vectors[vector_name1], vectors[vector_name2])

# Create an output filename
output_filename = f'name_p5_out{vector_name1}{vector_name2}.txt'

# Write the result to the output file
with open(output_filename, 'w') as f:
    f.write(str(result))

print(f"Dot product {vector_name1} ∙ {vector_name2} saved in {output_filename}")
