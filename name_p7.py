import numpy as np

# Define the vectors
vectors = {
    'r': np.array([-1, -2]),
    's': np.array([-3, 3]),
    'u': np.array([2, -1]),
    'v': np.array([3, 1]),
    'w': np.array([1, 3])
}

# List of matrix file names
matrix_files = ['jcortese_mat1.txt', 'jcortese_mat2.txt', 'jcortese_mat3.txt', 'jcortese_mat4.txt']

# Perform dot product calculations and save results to output files
for vector_name1 in vectors.keys():
    for vector_name2 in vectors.keys():
        if vector_name1 < vector_name2:
            # Calculate the dot product
            result = np.dot(vectors[vector_name1], vectors[vector_name2])

            # Create an output filename for dot product
            output_filename = f'name_p7_outD{vector_name1}{vector_name2}.txt'

            # Write the result to the output file
            with open(output_filename, 'w') as f:
                f.write(str(result))

            print(f"Dot product {vector_name1} ∙ {vector_name2} saved in {output_filename}")

# Perform matrix transpose and save results to output files
for i, input_file in enumerate(matrix_files):
    # Read the matrix from the input file
    matrix = np.loadtxt(input_file)

    # Transpose the matrix
    transposed_matrix = np.transpose(matrix)

    # Create the output file name for transpose
    output_file = f'name_p7_outT{i + 1}.txt'

    # Write the transposed matrix to the output file
    np.savetxt(output_file, transposed_matrix, fmt='%d')

    print(f"Matrix {i + 1} transposed and saved in {output_file}")
