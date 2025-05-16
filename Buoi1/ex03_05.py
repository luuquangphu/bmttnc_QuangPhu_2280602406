def x(n):
    count = {}
    for i in n:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

y = input("Nhập danh sách: ")

z = y.split()

c = x(z)

print("Số lần xuất hiện: ",c)