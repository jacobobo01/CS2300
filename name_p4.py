import numpy as np

# Function to read a matrix from a file
def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            # Parse each line into a list of floating-point numbers
            row = [float(x) for x in line.strip().split()]
            matrix.append(row)
    return matrix

# Function to write a matrix to a file
def write_matrix_to_file(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix:
            # Convert each row to a string and write to the file
            file.write(' '.join(map(str, row)) + '\n')

# Get user input for input matrix filenames
input_file_A = input('Enter the filename for matrix A: ')
input_file_B = input('Enter the filename for matrix B: ')

# Read matrices from input files using NumPy
matrix_A = np.array(read_matrix_from_file(input_file_A))
matrix_B = np.array(read_matrix_from_file(input_file_B))

# Check if the matrices have compatible dimensions for addition (A + B)
if matrix_A.shape != matrix_B.shape:
    print("Matrix addition is not possible. The matrices must have the same dimensions.")
else:
    # Perform matrix addition (A + B)
    result_addition = matrix_A + matrix_B

    # Create an output filename for matrix addition
    output_file_addition = f'name_p4_outA{input_file_A[-5]}{input_file_B[-5]}.txt'

    # Write the result of matrix addition to the output file
    write_matrix_to_file(result_addition, output_file_addition)

    print(f"Matrix Addition result saved in {output_file_addition}")

# Check if the matrices have compatible dimensions for multiplication (A * B)
if matrix_A.shape[1] != matrix_B.shape[0]:
    print("Matrix multiplication is not possible. The number of columns in matrix A must match the number of rows in matrix B.")
else:
    # Perform matrix multiplication (A * B)
    result_multiplication = np.dot(matrix_A, matrix_B)

    # Create an output filename for matrix multiplication
    output_file_multiplication = f'name_p4_outM{input_file_A[-5]}{input_file_B[-5]}.txt'

    # Write the result of matrix multiplication to the output file
    write_matrix_to_file(result_multiplication, output_file_multiplication)

    print(f"Matrix Multiplication result saved in {output_file_multiplication}")
