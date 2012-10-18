from Crypto.Cipher import AES
from Crypto import Random
import binascii

key = 'adnghtusylehfngkerthfndlotkjfhtu'
iv = "78e22430750291ea"

cipher = AES.new(key, AES.MODE_CFB, iv)
encrypted = cipher.encrypt('Attack at dawn').encode("hex")
print encrypted

decipher = AES.new(key, AES.MODE_CFB, iv)
decrypted = decipher.decrypt(encrypted.decode("hex"))
print decrypted