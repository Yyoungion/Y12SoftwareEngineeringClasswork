import hmac
import hashlib
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(encrypted_data)
    print(f"File {file_path} encrypted successfully.")

encrypt_file('U:\Software Engineering Y12\Classwork\Secure Software Architecture\Protect Against Attacks\Task 2\sensitive_data.txt')

# Decrypt the encrypted file
def decrypt_file(encrypted_file_path):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    original_file_path = encrypted_file_path.replace('.enc', '')
    with open(original_file_path, 'wb') as file:
        file.write(decrypted_data)
    print(decrypted_data)
    print(f"File {original_file_path} decrypted successfully.")

def constant_time_compare(val1, val2):
    return hmac.compare_digest(val1, val2)

# Example usage
user_input = input('Enter your password: ')

# Compute the SHA-256 hash of the correct password ('password123')
stored_hash = hashlib.sha256('password123'.encode()).hexdigest()

# Compute the SHA-256 hash of the user's input
user_input_hash = hashlib.sha256(user_input.encode()).hexdigest()

# Compare the stored hash with the user's input hash using constant-time comparison
if constant_time_compare(stored_hash, user_input_hash):
    # If the hashes match, authentication is successful
    print("Authentication successful.")
    decrypt_file('U:\Software Engineering Y12\Classwork\Secure Software Architecture\Protect Against Attacks\Task 2\sensitive_data.txt.enc')

else:
    # If the hashes do not match, authentication fails
    print("Authentication failed.")
