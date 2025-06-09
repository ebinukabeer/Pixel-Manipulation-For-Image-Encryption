
# Caesar Cipher Tool

A simple Python-based Caesar Cipher utility that allows users to **encrypt** or **decrypt** messages by shifting the letters of the alphabet.

## 🧩 What is Caesar Cipher?

The Caesar Cipher is one of the earliest and simplest encryption techniques. Each letter in the plaintext is shifted a fixed number of positions down or up the alphabet.

## 🚀 Features

* Encrypts text with a user-defined shift.
* Decrypts encrypted text using the same shift.
* Preserves case (uppercase/lowercase).
* Leaves non-alphabetic characters (like punctuation, numbers) unchanged.

## 📂 How to Use

1. Run the script using Python:

   python caesar_cipher.py


2. Choose whether to encrypt (`e`) or decrypt (`d`).

3. Enter your message.

4. Enter the shift value (integer).

### Example

Caesar Cipher Tool  
Type 'e' to encrypt or 'd' to decrypt: e  
Enter your message: Hello, World!  
Enter the shift value: 3  
Encrypted message: Khoor, Zruog!

To decrypt:

Type 'e' to encrypt or 'd' to decrypt: d  
Enter your message: Khoor, Zruog!  
Enter the shift value: 3  
Decrypted message: Hello, World!

## 📄 File Structure

* `caesar_cipher.py` – Main Python script with encryption and decryption logic.

## 🛠 Requirements

* Python 3.x
