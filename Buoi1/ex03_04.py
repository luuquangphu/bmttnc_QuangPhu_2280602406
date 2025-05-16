def x(n):
    q = n[0]
    w = n[1]
    return q, w

n = eval(input("Nhập: "))
q,w = x(n)

print("Đầu: ",q)
print("Cuối: ",w)