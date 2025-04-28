# def generate_pascals_triangle(n):
#     triangle = [[1] * (i + 1) for i in range(n)]
#
#     for i in range(2, n):  # Start from row index 2
#         for j in range(1, i):
#             triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#
#     return triangle
#
#
# # Input
# n = 5
# result = generate_pascals_triangle(n)
#
# # Print the triangle
# for row in result:
#     print(row)

def pascal_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    return triangle
print('\n')
n = 5
print(pascal_triangle(n))