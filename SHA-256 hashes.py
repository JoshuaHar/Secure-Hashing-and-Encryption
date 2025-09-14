import hashlib

def sha256_hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

def sha256_hash_file(filename):
    try:
        with open(filename, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except FileNotFoundError:
        print("File either does not exist, or it was spelt wrong.")
        quit()

if __name__ == "__main__":
    choice = input("Hash (1) text or (2) file? ")

    if choice == "1":
        text = input("Enter text: ")
        print("SHA-256:", sha256_hash_text(text))
    elif choice == "2":
        filename = input("Enter filename: ")
        print("SHA-256:", sha256_hash_file(filename))
    else:
        print("Answer must be 1 or 2.")
