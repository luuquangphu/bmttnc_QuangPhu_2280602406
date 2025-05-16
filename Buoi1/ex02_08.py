def chiahetcho5(sonhiphan):
    sothapphan = int(sonhiphan,2)
    if sothapphan % 5 == 0:
        return True
    else:
        return False

chuoinhiphan = input("Nhập chuỗi nhị phân (tách nhau bởi dấu phẩy): ")
chuoinhiphans = chuoinhiphan.split(',')

sochiahetcho5 = [so for so in chuoinhiphans if chiahetcho5(so)]

if len(sochiahetcho5) > 0:
    ketqua = ','.join(sochiahetcho5)
    print("Các số nhị phân chia hết cho 5 là: ",ketqua)
else:
    print("Không tồn tại số nhị phân nào chia hết cho 5!")
