from PIL import Image
import numpy as np

def load_image(image_path):
    try:
        image = Image.open(image_path)
        image.show()
        return image
    except IOError:
        print(f"Cannot open {image_path}. Make sure the file exists.")
        return None

def image_to_array(image):
    return np.array(image)

def array_to_image(array):
    return Image.fromarray(array.astype('uint8'))

def encrypt_image(image_array, key):
    image_array = image_array.astype('uint8')
    encrypted_array = np.bitwise_xor(image_array, key)
    return encrypted_array

def decrypt_image(encrypted_array, key):
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    return decrypted_array

def save_image(image, output_path):
    image.save(output_path)
    print(f"Image saved to {output_path}")

def show_image(image):
    image.show()

def main():
    image_path = r'C:\Users\jyoth\PycharmProjects\Prodigy cyber\image.jpg'
    image = load_image(image_path)
    if image is None:
        return

    image_array = image_to_array(image)
    key = 50  # Encryption key for XOR operation

    encrypted_array = encrypt_image(image_array, key)
    encrypted_image = array_to_image(encrypted_array)
    save_image(encrypted_image, 'encrypted_image.jpg')
    show_image(encrypted_image)

    decrypted_array = decrypt_image(encrypted_array, key)
    decrypted_image = array_to_image(decrypted_array)
    save_image(decrypted_image, 'decrypted_image.jpg')
    show_image(decrypted_image)

if __name__ == "__main__":
    main()
