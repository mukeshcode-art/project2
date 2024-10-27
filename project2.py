from PIL import Image
import numpy as np

def encrypt_image(image_path, shift):
    
    img = Image.open(image_path)
    img = img.convert('RGB')  
    
   
    img_array = np.array(img)
    
   
    encrypted_array = img_array + shift
    
    # Clip the values to stay within the range of uint8
    encrypted_array = np.clip(encrypted_array, 0, 255)
    
    # Convert back to image
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    return encrypted_img

def decrypt_image(encrypted_img, shift):
    # Convert encrypted image to numpy array
    encrypted_array = np.array(encrypted_img)
    
    # Decrypt by subtracting the shift value
    decrypted_array = encrypted_array - shift
    
    # Clip the values to stay within the range of uint8
    decrypted_array = np.clip(decrypted_array, 0, 255)
    
    # Convert back to image
    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    return decrypted_img

def main():
    print("Image Encryption Tool")
    choice = input("Would you like to (e)ncrypt or (d)ecrypt an image? ").lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice, please select 'e' for encryption or 'd' for decryption.")
        return

    image_path = input("Enter the path of the image: ")
    shift = int(input("Enter the shift value (integer): "))

    if choice == 'e':
        encrypted_img = encrypt_image(image_path, shift)
        encrypted_img.show()  # Show encrypted image
        encrypted_img.save("encrypted_image.png")
        print("Encrypted image saved as 'encrypted_image.png'")
    else:
        # For decryption, we assume the user provides an encrypted image file
        encrypted_img = Image.open(image_path)
        decrypted_img = decrypt_image(encrypted_img, shift)
        decrypted_img.show()  # Show decrypted image
        decrypted_img.save("decrypted_image.png")
        print("Decrypted image saved as 'decrypted_image.png'")

if __name__ == "__main__":
    main()
