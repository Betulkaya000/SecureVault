import os
import hashlib
import json
from cryptography.fernet import Fernet

MASTER_PASSWORD_FILE = 'data/master_password.hash'
PASSWORDS_FILE = 'data/passwords.json'
KEY_FILE = 'data/key.key'

def set_master_password(master_password):
    if not os.path.exists('data'):
        os.makedirs('data')
    hashed_password = hashlib.sha256(master_password.encode()).hexdigest()
    with open(MASTER_PASSWORD_FILE, 'w') as f:
        f.write(hashed_password)

def verify_master_password(master_password):
    if not os.path.exists(MASTER_PASSWORD_FILE):
        return False
    hashed_password = hashlib.sha256(master_password.encode()).hexdigest()
    with open(MASTER_PASSWORD_FILE, 'r') as f:
        stored_password = f.read()
    return hashed_password == stored_password

def generate_key(master_password):
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_FILE):
        return None
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def save_key(key):
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

def load_passwords(key):
    if not os.path.exists(PASSWORDS_FILE):
        return {}
    with open(PASSWORDS_FILE, 'rb') as passwords_file:
        encrypted_data = passwords_file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    return json.loads(decrypted_data)

def save_passwords(key, passwords):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(json.dumps(passwords).encode())
    with open(PASSWORDS_FILE, 'wb') as passwords_file:
        passwords_file.write(encrypted_data)