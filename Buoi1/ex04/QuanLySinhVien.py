from SinhVien import SV

class QLSV:
    lstSV = []

    def genID(self):
        maxId = 1
        if(self.QuantitySV() > 0):
            # Find the maximum ID in the current list
            maxId = self.lstSV[0].id
            for sv in self.lstSV:
                if(maxId < sv.id):
                    maxId = sv.id
            # Increment the maximum ID to get a new unique ID
            maxId += 1
        return maxId
    
    def QuantitySV(self):
        """Returns the number of students in the list."""
        return len(self.lstSV) # Using len() is more Pythonic than __len__()

    def inputSV(self):
        """Prompts the user for student details and adds a new student to the list."""
        id = self.genID()
        name = input("Tên: ")
        sex = input("Giới tính: ")
        major = input("Ngành: ")
        # Ensure input is a valid float, handle potential ValueError
        try:
            DTB = float(input("Điểm trung bình: "))
        except ValueError:
            print("Điểm trung bình không hợp lệ. Vui lòng nhập một số.")
            return # Exit if input is invalid

        sv = SV(id, name, sex, major, DTB)
        self.ratingRank(sv)
        self.lstSV.append(sv)
        print(f"Đã thêm sinh viên {name} với ID: {id}")

    def updateSV(self, svId):
        """Updates the information of a student by their ID."""
        sv:SV = self.findSVById(svId)
        if(sv != None):
            print(f"\nCập nhật thông tin cho sinh viên ID: {svId}")
            name = input(f"Tên mới (hiện tại: {sv.name}): ")
            sex = input(f"Giới tính mới (hiện tại: {sv.sex}): ")
            major = input(f"Ngành mới (hiện tại: {sv.major}): ")
            
            try:
                DTB = float(input(f"Điểm trung bình mới (hiện tại: {sv.DTB}): "))
            except ValueError:
                print("Điểm trung bình không hợp lệ. Không cập nhật điểm.")
                DTB = sv.DTB # Keep old DTB if new input is invalid

            sv.name = name
            sv.sex = sex
            sv.major = major
            sv.DTB = DTB
            self.ratingRank(sv)
            print(f"Đã cập nhật thông tin cho sinh viên ID: {svId} thành công!")
        else:
            print(f"Không tìm thấy sinh viên với ID: {svId}!")

    def sortById(self):
        self.lstSV.sort(key=lambda x: x.id, reverse=False)
        print("Danh sách sinh viên đã được sắp xếp theo ID.")
    
    def sortByName(self):
        # Using .lower() for case-insensitive sorting
        self.lstSV.sort(key=lambda x: x.name.lower(), reverse=False)
        print("Danh sách sinh viên đã được sắp xếp theo tên.")

    def sortByDTB(self):
        self.lstSV.sort(key=lambda x: x.DTB, reverse=False)
        print("Danh sách sinh viên đã được sắp xếp theo điểm trung bình.")

    def findSVById(self, svId):
        item = None
        if(self.QuantitySV() > 0):
            for sv in self.lstSV:
                if(sv.id == svId):
                    item = sv
                    break # Found the student, no need to continue
        return item

    def findSVByName(self, svName):
        result_list = []
        if(self.QuantitySV() > 0):
            for sv in self.lstSV:
                if(svName.upper() in sv.name.upper()):
                    result_list.append(sv)
        return result_list
        
    def DeleteSVById(self, svId):
        isDelete = False
        item = self.findSVById(svId)
        if(item != None):
            self.lstSV.remove(item) # Corrected to .remove()
            isDelete = True
            print(f"Sinh viên với ID: {svId} đã bị xóa.")
        else:
            print(f"Không tìm thấy sinh viên với ID: {svId} để xóa.")
        return isDelete

    def ratingRank(self, sv:SV):
        """Assigns a 'Học Lực' (academic performance) rank based on DTB."""
        if(sv.DTB >= 8):
            sv.HL = "Giỏi"
        elif(sv.DTB >= 6.5): 
            sv.HL = "Khá"
        elif(sv.DTB >= 5):
            sv.HL = "Trung Bình"
        else:
            sv.HL = "Yếu"
        
    def showSV(self, lstSV_to_show):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name","Sex","Major","DTB", "Học Lực"))
        print("-" * 70)
        if(len(lstSV_to_show) > 0): 
            for sv in lstSV_to_show:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv.id, sv.name, sv.sex, sv.major, sv.DTB, sv.HL))
        else:
            print("Không có sinh viên nào để hiển thị.")
        print("\n")

    def getlstSV(self):
        """Returns the entire list of students."""
        return self.lstSV
