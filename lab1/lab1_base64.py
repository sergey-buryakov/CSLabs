import base64
from lab1_qtyInformation import ReadFile, FindAvarangeEntropy, FindFrequencyAndNumberChars

def encode(data):
    n2ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    buf = ""
    data = bytearray(data)
    rem = len(data) % 3
    pad = 3 - rem
    if rem > 0:
        data.append(0)
        for i in range(pad):
            data.append(0)
    for i in range(2, len(data), 3):
        b3 = (data[i-2] << 16) | (data[i - 1] << 8) | data[i]
        buf += n2ch[b3 >> 18] + n2ch[(b3 >> 12) & 0x3f]
        buf += n2ch[(b3 >> 6) & 0x3f] + n2ch[b3 & 0x3f]
    if rem > 0: 
        buf = buf[:-pad] + "=" * pad
    return buf

def ReadFileBin(filename):
    with open(filename, "rb") as file:
        byte = file.read()
    return byte

def qtyInfo(data):
    freq, number = FindFrequencyAndNumberChars(data)
    return round(FindAvarangeEntropy(freq) * number / 8)

file = "lab1/PCI"

text = ReadFile(file).encode()
enc1 = encode(text)
print(enc1)
print(qtyInfo(enc1),"bytes")

encbin = encode(ReadFileBin(file + ".bz2"))
print(qtyInfo(encbin),"bytes")

# to compare result of custom encode function with built in
# enc2 = base64.b64encode(text).decode()
# for i in range(len(enc2)):
#     if enc1[i] != enc2[i]:
#         print("i = {0}, enc1 = '{1}' enc2 = '{2}'".format(i,enc1[i],enc2[i]))