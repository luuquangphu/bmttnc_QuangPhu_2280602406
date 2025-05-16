inputx = int(input("Nhập X: "))
inputy = int(input("Nhập Y: "))

n = inputx
m = inputy

a = [[0 for col in range(m)] for row in range(n)]

for row in range(n):
    for col in range(m):
        a[row][col] = row * col

print(a)