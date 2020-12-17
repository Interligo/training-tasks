# Матрица, последовательно заполняющаяся числами по спирали, размером n * n

def draw_matrix(matrix_size: int):
    """Функция для построения матрицы необходимого размера."""
    n = matrix_size
    matrix = [[0 for j in range(n)] for i in range(n)]
    num = 1
    contour = 0  # Переменная для сужения контура матрицы
    row = n  # i
    column = n  # j

    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    elif n > 1:
        while num != n * n + 1:
            for i in range(0 + contour, int(row / row) + contour):
                for j in range(0 + contour, column - contour):
                    if matrix[i][j] == 0:
                        matrix[i][j] = num
                        num += 1
            for j in range(column - 1 - contour, column - contour):
                for i in range(int(row / row) + contour, row - contour):
                    if matrix[i][j] == 0:
                        matrix[i][j] = num
                        num += 1
            for i in range(row - 1 - contour, row - contour):
                for j in range(-2 - contour, -column - 1 + contour, -1):
                    if matrix[i][j] == 0:
                        matrix[i][j] = num
                        num += 1
            for j in range(0 + contour, int(column / column) + contour):
                for i in range(-2 - contour, -row + contour, -1):
                    if matrix[i][j] == 0:
                        matrix[i][j] = num
                        num += 1
            contour += 1

        print_matrix(matrix_size, matrix)


def print_matrix(matrix_size: int, matrix: list):
    """Функция для отрисовки матрицы."""
    for i in range(matrix_size):
        for j in range(matrix_size):
            print(matrix[i][j], end=' ')
        print()


if __name__ == '__main__':
    while True:
        n = input('Укажите размер матрицы (число): ')

        if n.isdigit():
            draw_matrix(int(n))
            break
