#coding:utf-8
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from binascii import unhexlify
from binascii import b2a_hex,a2b_hex


def encrypt(iv,plaintext):
    if len(plaintext)%16 != 0:
        print("plaintext length is invalid")
        return
    if len(iv) != 16:
        print("IV length is invalid")
        return
    key="1234567890123456"
    aes_encrypt = AES.new(key.encode("utf-8"),AES.MODE_CBC,iv.encode("utf-8"))
    return aes_encrypt.encrypt(plaintext.encode("utf-8")).hex()

def decrypt(iv,cipher):
    if len(iv) != 16:
        print("IV length is invalid")
        return
    key="1234567890123456"
    aes_decrypt = AES.new(key.encode("utf-8"),AES.MODE_CBC,iv.encode("utf-8"))
    paddedParams = aes_decrypt.decrypt(unhexlify(cipher))
    return b2a_hex(aes_decrypt.decrypt(a2b_hex(cipher)))


def test():
    iv="ABCDEFGH12345678"
    plaintext="0123456789ABCDEFhellocbcflipping"
    cipher=encrypt(iv, plaintext)
    print("cipher:",cipher)
    de_cipher = decrypt(iv, cipher)
    print("de_cipher:",de_cipher)
    bin_cipher = bytearray(a2b_hex(cipher))
    
    # bin_cipher[15] = bin_cipher[15] ^ ord('g') ^ ord('G')
    # print("-----------------")
    # print(bin_cipher)

    # de_cipher2 = decrypt(iv,b2a_hex(bin_cipher))
    # print("de_cipher2:",de_cipher2)
    # print(a2b_hex(de_cipher2))

    str = "4913ceb9d0a80cfe38a0d5f633c63eb27f1c833277f85bc2bf628cb7e0641851"
    bin_cipher = bytearray(a2b_hex(str))
    bin_cipher[15] = bin_cipher[15] ^ ord('g') ^ ord('G')
    de_cipher2 = decrypt(iv,b2a_hex(bin_cipher))
    print("de_cipher2:",a2b_hex(de_cipher2))

    
test()