from PIL import Image
import numpy as np

# Use a fixed XOR key for encryption/decryption
KEY = 123

def encrypt_image(input_path, output_path):
    img = Image.open(input_path)
    arr = np.array(img)
    encrypted_arr = arr ^ KEY
    encrypted_img = Image.fromarray(encrypted_arr.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path):
    img = Image.open(input_path)
    arr = np.array(img)
    decrypted_arr = arr ^ KEY
    decrypted_img = Image.fromarray(decrypted_arr.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("=== PixelCryptXOR: Simple Image Encryptor ===")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Enter your choice (1/2): ")

    input_path = input("Enter input image path (e.g. input.jpg): ")
    output_path = input("Enter output image path (e.g. output.jpg): ")

    if choice == '1':
        encrypt_image(input_path, output_path)
    elif choice == '2':
        decrypt_image(input_path, output_path)
    else:
        print("Invalid choice!")

if _name_ == "_main_":
    main()
