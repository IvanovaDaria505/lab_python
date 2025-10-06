def flatten(mat: list[list | tuple]) -> list:
    a=[]
    for i in mat:
        for m in i:
            if str(m) in '0123456789':
                a.append(m)
            else:
                print('TypeError')
    return a 
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))   