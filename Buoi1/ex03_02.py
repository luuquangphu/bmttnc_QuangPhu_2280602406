def daonguocsolst(lst):
    return lst[::-1]

inputlst = input("Nhập danh sách số cần đảo ngược: ")
n = list(map(int, inputlst.split(',')))

kq = daonguocsolst(n)
print("Danh sách số đã đảo ngược: ",kq)
