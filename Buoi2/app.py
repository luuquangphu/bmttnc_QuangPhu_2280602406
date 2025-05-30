from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher() 

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    plain_text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return render_template('caesar.html', encrypted_text=encrypted_text)

@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    cipher_text = request.form['inputCipherText']
    key = int(request.form['inputKeyPlain'])
    
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return render_template('caesar.html', decrypted_text=decrypted_text)

# --- Routes cho Vigenere Cipher ---
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    plain_text = request.form['inputPlainText']
    key = request.form['inputKeyPlain'] 
    
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return render_template('vigenere.html', encrypted_text=encrypted_text)

@app.route("/vigenere/decrypt", methods=['POST']) # Đã đổi route
def vigenere_decrypt():
    cipher_text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return render_template('vigenere.html', decrypted_text=decrypted_text)

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    plain_text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain']) 
    
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return render_template('railfence.html', encrypted_text=encrypted_text)

@app.route("/railfence/decrypt", methods=['POST']) # Đã đổi route
def railfence_decrypt():
    cipher_text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return render_template('railfence.html', decrypted_text=decrypted_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)