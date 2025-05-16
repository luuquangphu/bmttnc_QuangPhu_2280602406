def tingTongSoChan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong


inputlst = input("Nhập danh sách sô:")

x = list(map(int, inputlst.split(',')))

kq = tingTongSoChan(x)

print("Tổng của các số trong danh sách mà chia hết cho 2 là: ",kq)