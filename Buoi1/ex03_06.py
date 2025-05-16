def x(dic,k):
    if k in dic:
        del dic[k]
        return True
    else:
        return False

y = {'a': 1,'b': 2,'c' : 3, 'd' : 4}

z = 'b'

kq = x(y,z)

if kq:
    print("Phần tử đã được xoá khỏi dic: ",y)
else:
    print("Không tìm thấy phần tử cần xoá!")