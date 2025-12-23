if __name__ == "__main__":
    pass
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:4}" for num in row))

def sum_diagonal(matrix, diagonal_type):
    n = len(matrix)
    total_sum = 0
    
    if diagonal_type == 'main':
            for i in range(n):
            total_sum += matrix[i][i]
    elif diagonal_type == 'side'
        for i in range(n):
            total_sum += matrix[i][n - 1 - i]
    else:
        raise ValueError("Неверный тип диагонали. Выберите 'main' или 'side'")
    
    return total_sum

def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Исходная матрица:")
    print_matrix(matrix)
    choice = input("\nВыберите диагональ для подсчета суммы:\n"
                  "1 - Главная диагональ\n"
                  "2 - Побочная диагональ\n"
                  "Ваш выбор (1 или 2): ")
    if choice == '1':
        diagonal_type = 'main'
    elif choice == '2':
        diagonal_type = 'side'
    else:
        print("Неверный выбор!")
        return
    try:
        result = sum_diagonal(matrix, diagonal_type)
        print(f"\nСумма элементов {diagonal_type} диагонали: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
if __name__ == "__main__":
    main()
