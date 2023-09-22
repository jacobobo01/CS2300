# Get first and last name
first_name = 'Jacob'
last_name = 'Cortese'

# Print lengths
print(first_name, len(first_name))
print(last_name, len(last_name))

# Matrix 1
# Set dimensions based on name lengths
rows1 = len(last_name)
cols1 = len(first_name)

# Create matrix as nested list
mat1 = [[0 for j in range(cols1)] for i in range(rows1)]

# Initialize value
val = 1

# Fill matrix iterating cols first
for j in range(cols1):
    for i in range(rows1):
        mat1[i][j] = val
        val += 1

# Write matrix to file
with open('jcortese_mat1.txt', 'w') as f:
    for row in mat1:
        f.write(' '.join([str(x) for x in row]) + '\n')

# Matrix 2
# Set dimensions
rows2 = len(last_name)
cols2 = len(first_name)

# Create empty matrix
mat2 = [[0 for j in range(cols2)] for i in range(rows2)]

# Initialize value
val = 2

# Fill matrix iterating rows first
for i in range(rows2):
    for j in range(cols2):
        mat2[i][j] = val
        val += 3

# Write to file
with open('jcortese_mat2.txt', 'w') as f:
    for row in mat2:
        f.write(' '.join([str(x) for x in row]) + '\n')

# Matrix 3
# Set dimensions
rows3 = 2
cols3 = 4

# Create empty matrix
mat3 = [[0 for j in range(cols3)] for i in range(rows3)]

# Initialize value
val = 10

# Fill matrix iterating cols first
for j in range(cols3):
    for i in range(rows3):
        mat3[i][j] = val
        val -= 2

# Write to file
with open('jcortese_mat3.txt', 'w') as f:
    for row in mat3:
        f.write(' '.join([str(x) for x in row]) + '\n')

# Matrix 4
# Set dimensions
rows4 = 4
cols4 = 2

# Create empty matrix
mat4 = [[0 for j in range(cols4)] for i in range(rows4)]

# Initialize value
val = -6

# Fill matrix iterating rows first
for i in range(rows4):
    for j in range(cols4):
        mat4[i][j] = val
        val += 1.5

# Write to file
with open('jcortese_mat4.txt', 'w') as f:
    for row in mat4:
        f.write(' '.join(['%.1f' % x for x in row]) + '\n')
