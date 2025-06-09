def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Main program
print("Caesar Cipher Tool")
choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

if choice in ['e', 'd']:
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted = encrypt(message, shift)
        print("Encrypted message:", encrypted)
    else:
        decrypted = decrypt(message, shift)
        print("Decrypted message:", decrypted)
else:
    print("Invalid choice. Please enter 'e' or 'd'.")
