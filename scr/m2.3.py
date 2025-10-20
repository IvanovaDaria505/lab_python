def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []  
    f = len(mat[0])
    for r in mat:
        if len(r) != f:
            raise ValueError
    w = []
    for j in range(len(mat[0])):
        col_sum = 0
        for i in range(len(mat)):
            col_sum += mat[i][j]
        w.append(col_sum)
    return w
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
