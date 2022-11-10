n = int(input())
date = [[int(num) for num in input().split()] for _ in range(n)]


def num_check(matrix, size):
    num_magic = list(range(1, size ** 2 + 1))
    num_matrix = sorted([num for row in matrix for num in row])
    return num_magic == num_matrix


def row_check(matrix):
    main_sum = sum(matrix[0])
    result = True
    for r in matrix:
        if sum(r) != main_sum:
            result = False
            break
    return result


def col_check(matrix, size):
    col_sum = 0
    for i in matrix:
        col_sum += i[0]
    for row in matrix:
        temp = 0
        for c in range(size):
            temp += row[c]
        if temp != col_sum:
            return False
        return True


def diag_check(matrix, size):
    main_diag = sum([matrix[i][i] for i in range(size)])
    side_diag = sum([matrix[i][size - 1 - i] for i in range(size)])
    return main_diag == side_diag


if num_check(date, n) and row_check(date) and col_check(date, n) and diag_check(date, n):
    print('YES')
else:
    print('NO')
