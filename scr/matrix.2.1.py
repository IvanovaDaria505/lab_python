def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []  
    f = len(mat[0])
    for r in mat:
        if len(r) != f:
            raise ValueError
    n= []
    for j in range(len(mat[0])):
        t = []
        for i in range(len(mat)):
            t.append(mat[i][j])
        n.append(t)
    return n
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
