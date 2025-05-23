from QuanLySinhVien import QLSV

qlsv = QLSV()
while (1 == 1):
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("********************MENU********************")
    print("*** 1. Them sinh vien.")
    print("*** 2. Cap nhat thong tin sinh vien boi ID.")
    print("*** 3. Xoa sinh vien boi ID.")
    print("*** 4. Tim kiem sinh vien theo ten.")
    print("*** 5. Sap xep sinh vien theo diem trung binh.")
    print("*** 6. Sap xep sinh vien theo ten chuyen nganh.")
    print("*** 7. Hien thi danh sach sinh vien.")
    print("*** 0. Thoat")
    print("********************************************")

    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them sinh vien.")
        qlsv.inputSV()
        print("\nThem sinh vien thanh cong!")
    # This 'elif' needs to be at the same indentation level as the 'if' above
    elif (key == 2):
        if (qlsv.QuantitySV() > 0):
            print("\n2. Cap nhat thong tin sinh vien. ")
            print("\nNhap ID: ")
            ID = int(input())
            qlsv.updateSV(ID)
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 3):
        if (qlsv.QuantitySV() > 0):
            print("\n3. Xoa sinh vien.")
            print("\nNhap ID: ")
            ID = int(input())
            if (qlsv.DeleteSVById(ID)):
                print(f"\nSinh vien co id = {ID}, da bi xoa.")
            else:
                print(f"\nSinh vien co id = {ID}, khong ton tai.")
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 4):
        if (qlsv.QuantitySV() > 0):
            print("\n4. Tim kiem sinh vien theo ten.")
            print("\nNhap ten de tim kiem: ")
            name = input()
            searchResult = qlsv.findSVByName(name)
            qlsv.showSV(searchResult)
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 5):
        if (qlsv.QuantitySV() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDTB()
            qlsv.showSV(qlsv.getlstSV())
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 6):
        if (qlsv.QuantitySV() > 0):
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSV(qlsv.getlstSV())
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 7):
        if (qlsv.QuantitySV() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSV(qlsv.getlstSV())
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chu nang trong hop menu.")