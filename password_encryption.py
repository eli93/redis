from passlib.context import CryptContext

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)


def encrypt_password(password, file_name):
    hashed = pwd_context.encrypt(password)
    file_name.write(hashed + '\n')
    return hashed


def check_encrypted_password(password, hashed):
    acc = pwd_context.verify(password, hashed)
    return acc
