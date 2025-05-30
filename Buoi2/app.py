from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher # Đảm bảo đường dẫn import này đúng

app = Flask(__name__)

# Khởi tạo CaesarCipher (nếu bạn chưa làm)
caesar_cipher_instance = CaesarCipher() # Đổi tên biến để tránh trùng với tên lớp

# ... (các route khác của bạn)

@app.route("/caesar")
def caesar():
    # Khi truy cập trang lần đầu, không có kết quả nào để hiển thị
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    plain_text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    encrypted_text = caesar_cipher_instance.encrypt_text(plain_text, key) # Sử dụng instance đã tạo
    
    # Render lại template caesar.html và truyền kết quả mã hóa vào
    return render_template('caesar.html', encrypted_text=encrypted_text)

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    cipher_text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    decrypted_text = caesar_cipher_instance.decrypt_text(cipher_text, key) # Sử dụng instance đã tạo
    
    # Render lại template caesar.html và truyền kết quả giải mã vào
    return render_template('caesar.html', decrypted_text=decrypted_text)

# ... (phần main function của bạn)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)