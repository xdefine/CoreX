# encryption_tool.py
from Crypto.Cipher import AES
import base64
import os

def pad(s): return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
def unpad(s): return s[:-ord(s[len(s)-1:])]

def encrypt(message, key):
    key = key.ljust(16)[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(pad(message).encode())).decode()

def decrypt(enc, key):
    key = key.ljust(16)[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(base64.b64decode(enc)).decode())
