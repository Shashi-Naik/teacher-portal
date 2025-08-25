import hashlib, os, secrets

def hash_password(password, salt=None):
    
    if not salt:
        salt = os.urandom(16).hex()
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return hashed, salt

def create_token():
    return secrets.token_hex(32)

def add_marks(existing, new):
    total = existing + new
    return total if total <= 100 else None




