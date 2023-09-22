# Get first and last name
first_name = 'Jacob'
last_name = 'Cortese'

# Get user input for matrix names
mat1 = input('Enter first matrix name (Mat1, Mat2, Mat3, Mat4): ')
mat2 = input('Enter second matrix name (Mat1, Mat2, Mat3, Mat4): ')

# Open first input matrix file
with open('jcortese_' + mat1 + '.txt') as f:
    # Read lines and convert to nested list
    lines = f.readlines()
    A = [[float(num) for num in line.strip().split()] for line in lines]

# Open second input matrix file
with open('jcortese_' + mat2 + '.txt') as f:
    # Read lines and convert to nested list
    lines = f.readlines()
    B = [[float(num) for num in line.strip().split()] for line in lines]

# Check that dimensions match
if len(A) != len(B) or len(A[0]) != len(B[0]):
    print('Error - input matrices must have the same dimensions')
else:
    # Initialize result matrix
    rows = len(A)
    cols = len(A[0])
    C = [[0 for j in range(cols)] for i in range(rows)]

    # Add matrices element-wise
    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] + B[i][j]

    # Construct output file name
    outfile = 'jcortese_p2_out' + mat1[-1] + mat2[-1] + '.txt'

    # Write result matrix to file
    with open(outfile, 'w') as f:
        for row in C:
            f.write(' '.join([str(num) for num in row]) + '\n')

    print('Result written to', outfile)