def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []  
    f = len(mat[0])
    for r in mat:
        if len(r) != f:
            raise ValueError
    return [sum(row) for row in mat] 
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))     
