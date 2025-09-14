import string

def caesar_encrypt(text, shift=3):
    alphabet = string.ascii_lowercase
    result = []
    for char in text.lower():
        if char in alphabet:
            idx = (alphabet.index(char) + shift) % 26
            result.append(alphabet[idx])
        else:
            result.append(char)
    return "".join(result)

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    choice = input("(1) Encrypt or (2) Decrypt? ")
    if choice == "1":
        text = input("Enter text: ")
        try:
            shift = int(input("Enter shift value: "))
        except ValueError:
            print("Please enter a valid integer.")
            quit()
        print("Encrypted:", caesar_encrypt(text, shift))
    elif choice == "2":
        text = input("Enter text: ")
        try:
            shift = int(input("Enter shift value: "))
        except ValueError:
            print("Please enter a vlaid integer.")
            quit()
        print("Decrypted:", caesar_decrypt(text, shift))
    else:
        print("Answer must be 1 or 2.")