from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from binascii import unhexlify
from binascii import b2a_hex,a2b_hex


key="1234567890123456".encode()
iv="ABCDEFGH12345678".encode()

def encrypt_data(data):
	padded = pad(data.encode(),16,style='pkcs7')
	cipher = AES.new(key, AES.MODE_CBC,iv)
	enc = cipher.encrypt(padded)
	return enc.hex()

def decrypt_data(encryptedParams):
	cipher = AES.new(key, AES.MODE_CBC,iv)
	paddedParams = cipher.decrypt( unhexlify(encryptedParams))
	return paddedParams
src = "logged_username=admin&password=G0ld3n_b0y"
encrypt = encrypt_data(src)
print(encrypt)

s1 = "8eb818f08f61a25a7ed98f95d9d02558510a6971e3cc4f907be7c1094ca81e99eb60b752c42bc0d504193cb3684d5bf1"
decrypt = "logged_username=admin&password=G0ld3n_b0y"
bin_cipher = bytearray(a2b_hex(s1))
bin_cipher[15] = bin_cipher[15] ^ ord(decrypt[31]) ^ ord('g')
print(b2a_hex(bin_cipher))
de_cipher2 = decrypt_data(b2a_hex(bin_cipher))
print("de_cipher2:",de_cipher2)
