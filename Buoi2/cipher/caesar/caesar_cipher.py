from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self._alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self._alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            # Handle characters not in the alphabet (e.g., spaces, punctuation)
            if letter not in self._alphabet:
                encrypted_text.append(letter)
                continue

            letter_index = self._alphabet.index(letter)
            output_index = (letter_index + key) % alphabet_len
            output_letter = self._alphabet[output_index]
            encrypted_text.append(output_letter)
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self._alphabet)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            # Handle characters not in the alphabet (e.g., spaces, punctuation)
            if letter not in self._alphabet:
                decrypted_text.append(letter)
                continue

            letter_index = self._alphabet.index(letter)
            output_index = (letter_index - key) % alphabet_len
            output_letter = self._alphabet[output_index]
            decrypted_text.append(output_letter)
        return "".join(decrypted_text)