# Encryption function
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result


# Decryption function
def decrypt(text, shift):
    return encrypt(text, -shift)


# Main program
def main():
    choice = input("Do you want to encrypt or decrypt the message? (e/d): ").lower()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (number): "))
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print("Encrypted Message:", encrypted_message)
    elif choice == 'd':
        decrypted_message = encrypt(message, -shift)
        print("Decrypted Message:", decrypted_message)
    else:
        print("Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")


if __name__ == "__main__":
    main()
