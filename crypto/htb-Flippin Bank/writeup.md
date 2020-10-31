此题考察的是AES的CBC字节反转问题。
题目的名字给的提示Flippin，就应该想到字节反转了。

首先根据代码分析，用户名是admin，密码是g0ld3n_b0y，但是输入这个两个提示You cannot login as an admin from an external IP.\nYour activity has been logged. Goodbye!\n
输入其他的会显示"logged_username="+用户名+"&password="+密码的密文 比如（logged_username=admin&password=G0ld3n_b0y）
题目中AES的CBC是16个字节分为一组，那么明文16字节分组就如下所示：
logged_username=
admin&password=G
0ld3n_b0y

这个分组很有技巧，因为判断密码的算法是b'admin&password=g0ld3n_b0y' in unpad(paddedParams,16,style='pkcs7')  而对前面logged_username=的值不在意，因此可以考虑对admin及后面的内容进行反转。由于iv是随机生成的，我们并不掌握，因此无法完整的把logged_username=admin&password=g0ld3n_b0y进行反转，只能反转后两组。而本题中，只要反转任意一个字符就可以了。因此构造密码：G0ld3n_b0y，想办法将G反转为g
代码如下：
其中s1为logged_username=admin&password=G0ld3n_b0y的密文，将第32位与第16位进行异或再与'g'进行异或即可将G变成g。然后输出密文，将密文输入到程序里即可得flag。

```python
s1 = "8eb818f08f61a25a7ed98f95d9d02558510a6971e3cc4f907be7c1094ca81e99eb60b752c42bc0d504193cb3684d5bf1"
decrypt = "logged_username=admin&password=G0ld3n_b0y"
bin_cipher = bytearray(a2b_hex(s1))
bin_cipher[15] = bin_cipher[15] ^ ord(decrypt[31]) ^ ord('g')
print(b2a_hex(bin_cipher))
```
