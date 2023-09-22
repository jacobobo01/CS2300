# Function to transpose a matrix
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# List of matrix file names
matrix_files = ['jcortese_mat1.txt', 'jcortese_mat2.txt', 'jcortese_mat3.txt', 'jcortese_mat4.txt']

# Loop through the matrix files, transpose the matrices, and write them to output files
for i, input_file in enumerate(matrix_files):
    # Read the matrix from the input file
    with open(input_file, 'r') as f:
        matrix = [[float(num) for num in line.split()] for line in f.readlines()]

    # Transpose the matrix
    transposed_matrix = transpose_matrix(matrix)

    # Create the output file name
    output_file = f'name_p6_mat{i + 1}.txt'

    # Write the transposed matrix to the output file
    with open(output_file, 'w') as f:
        for row in transposed_matrix:
            f.write(' '.join([str(x) for x in row]) + '\n')

    print(f"Matrix {i + 1} transposed and saved in {output_file}")
