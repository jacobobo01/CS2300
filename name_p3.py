# Get user input for input matrix filenames and output filename
input_file_A = input('Enter the filename for matrix A: ')
input_file_B = input('Enter the filename for matrix B: ')
output_file = input('Enter the filename for the output matrix (A*B): ')

# Function to read a matrix from a file
def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            # Parse each line into a list of floating-point numbers
            row = [float(x) for x in line.strip().split()]
            matrix.append(row)
    return matrix

# Function to multiply two matrices
def multiply_matrices(matrix_A, matrix_B):
    rows_A = len(matrix_A)
    cols_A = len(matrix_A[0])
    rows_B = len(matrix_B)
    cols_B = len(matrix_B[0])

    # Check if the matrices can be multiplied
    if cols_A != rows_B:
        return None

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                # Multiply and accumulate the product
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]

    return result

# Read matrices from input files
matrix_A = read_matrix_from_file(input_file_A)
matrix_B = read_matrix_from_file(input_file_B)

# Perform matrix multiplication
result_matrix = multiply_matrices(matrix_A, matrix_B)

if result_matrix is None:
    print("Error: Matrices cannot be multiplied due to incompatible dimensions.")
else:
    # Write the result matrix to the output file
    with open(output_file, 'w') as file:
        for row in result_matrix:
            # Convert each row to a string and write to the file
            file.write(' '.join(map(str, row)) + '\n')

    print(f"Matrix multiplication result saved in {output_file}")
