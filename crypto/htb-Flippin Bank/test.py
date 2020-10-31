from binascii import unhexlify
from binascii import b2a_hex,a2b_hex

str = "07eadcd34fda91c76d688097133884b8541ea8541c1472e6de1849e15c8d46cd0cd1b3cd88b84fe857e562b5b63ef7ef"
bin_cipher = bytearray(a2b_hex(str.encode()))
for i in range(16,32):
    bin_cipher[i] = bin_cipher[i] ^ ord('1') ^ ord('0')
    print(b2a_hex(bin_cipher))
