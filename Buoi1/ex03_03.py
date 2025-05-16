def tuplelst(lst):
    return tuple(lst)

x = input("Nhập danh sách các số: ")
n = list(map(int, x.split(',')))

a = tuplelst(n)

print("List: ",n)
print("Tuple: ",a)