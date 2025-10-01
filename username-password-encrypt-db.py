# Code Structure of real Auth
# 
# def register(user, password):
#     encrypted_password = encrypt_password(password)
#     save_user(user, encrypted_password)

# def login(user, password):
#     stored_password = get_password_from_db(user)
#     encrypted_password = encrypt_password(password)
#     if stored_password != encrypted_password:
#         return "Incorrect Password"

import hashlib

# def encrypt_password( password ):
#     m = hashlib.sha256()
#     m.update(password.encode())
#     return m.hexdigest()

if __name__ == "__main__":
    password = "secret"
    # encrypted_password = encrypt_password(password)
    # print(encrypt_password)

    salt = "a1b2c3"
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100000) #encrypt 1,00,000 times
    print(dk.hex())