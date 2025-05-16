giolam = float(input("Nhập giờ làm: "))
luonggio = float(input("Nhập lương của 1 giờ làm: "))

giolamtoida = 44
tangca = max(0,giolam - giolamtoida)

luong = float((giolamtoida * luonggio) + (tangca * luonggio * 1.5))

print("Số tiền lương của nhân viên: ",luong)
