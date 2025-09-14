import subprocess
import os

def generate_keys():
    if not os.path.exists("private.pem"):
        subprocess.run(["openssl", "genpkey", "-algorithm", "RSA", "-out", "private.pem"])
        subprocess.run(["openssl", "rsa", "-pubout", "-in", "private.pem", "-out", "public.pem"])
        print("Generated RSA key pair: private.pem & public.pem")

def sign_message(message, signature_file="signature.bin"):
    with open("message.txt", "w") as f:
        f.write(message)
    subprocess.run(["openssl", "dgst", "-sha256", "-sign", "private.pem", "-out", signature_file, "message.txt"])
    print("Message signed ->", signature_file)

def verify_signature(signature_file="signature.bin"):
    result = subprocess.run(
        ["openssl", "dgst", "-sha256", "-verify", "public.pem", "-signature", signature_file, "message.txt"],
        capture_output=True,
        text=True
    )
    print("Verification result:", result.stdout.strip())

if __name__ == "__main__":
    generate_keys()

    message = input("Enter a message to sign: ")
    sign_message(message)

    verify_signature()