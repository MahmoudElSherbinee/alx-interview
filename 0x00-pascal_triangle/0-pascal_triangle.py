def pascal_triangle(n):
    if n <= 0:
        return
    triangle = [[1]]
    for x in range(n - 1):
        row = [1]
        for y in range(x):
            row.append(triangle[-1][y] + triangle[-1][y + 1])
        row.append(1)
        triangle.append(row)
    return triangle
