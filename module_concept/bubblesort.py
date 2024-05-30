# def bs(a):
#     b = len(a) - 1
#     for x in range(b):
#         for y in range(b - x):
#             if a[y] > a[y + 1]:  # Correct the swapping condition
#                 a[y], a[y + 1] = a[y + 1], a[y]

# a = [32, 5, 3, 6, 7, 54, 87]
# bs(a)
# print("Sorted list:", a)

rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    print('*' * i)
