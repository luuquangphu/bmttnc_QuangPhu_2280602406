print("Nhập văn bản(nhập done để kết thúc): ")
lines = []

while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("Các dòng đã nhập chuyển thành in hoa: ")
for line in lines:
    print(line.upper())