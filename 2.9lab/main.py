if __name__ == "__main__":
    pass
def create_identity_matrix(n):
    matrix = []
    for i in range(n):
        row = [0] * n
        row[i] = 1
        matrix.append(row)
    return matrix
def read_matrices(filename, n):
    matrices = []
    with open(filename, 'r') as file:
        current_matrix = []
        for line in file:
            numbers = list(map(int, line.strip().split()))
            current_matrix.append(numbers)
            if len(current_matrix) == n:
                matrices.append(current_matrix)
                current_matrix = []
    return matrices

def write_matrices(filename, matrices):
    with open(filename, 'w') as file:
        for matrix in matrices:
            for row in matrix:
                file.write(' '.join(map(str, row)) + '\n')
            file.write('\n')

n = int(input("Введите размерность матриц n: "))


matrices1 = read_matrices('file1.txt', n)
matrices2 = read_matrices('file2.txt', n)

k = len(matrices1)
l = len(matrices2)

# Проверяем условие k ≠ 1
if k != 1:
    if k < l:
        for _ in range(l - k):
            matrices1.append(create_identity_matrix(n))
    elif l < k:
        for _ in range(k - l):
            matrices2.append(create_identity_matrix(n))
write_matrices('file1.txt', matrices1)
write_matrices('file2.txt', matrices2)
print("Содержимое первого файла:")
for i, matrix in enumerate(matrices1):
    print(f"Матрица {i+1}:")
    for row in matrix:
        print(' '.join(map(str, row)))
    print()

print("\nСодержимое второго файла:")
for i, matrix in enumerate(matrices2):
    print(f"Матрица {i+1}:")
    for row in matrix:
        print(' '.join(map(str, row)))
    print()
