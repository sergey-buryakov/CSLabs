import struct

getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]

def floatToBinary64(value):
    val = struct.unpack('Q', struct.pack('d', value))[0]
    sign = str(0)
    exp = None
    mantisa = None
    binVal = getBin(val)
    if value >= 0:
        exp = binVal[:11]
        mantisa = binVal[11:]
    else:
        sign = str(1)
        exp = binVal[1:12]
        mantisa = binVal[12:]
    return sign, exp, mantisa

def binaryToFloat(value):
    hx = hex(int(value, 2))
    hx = int(hx, 16)
    st = struct.pack("Q", hx)
    return struct.unpack("d", st)[0]

def floatingMultiplication(value1, value2):
    sign1, exp1, mantissa1 = floatToBinary64(value1)
    sign2, exp2, mantissa2 = floatToBinary64(value2)
    print("Multiplier = {},\nMultiplicand = {}".format(sign1+exp1+mantissa1, sign2+exp2+mantissa2))
    signr = int(sign1) ^ int(sign2)
    print("The signed bit of the multiplicand is XOR'd with the multiplier signed bit. The result is put into the resultant sign bit: ", signr)
    mantissar = int("1" + mantissa1,2)*int("1" + mantissa2,2)
    print("The mantissa of the multiplier and multiplicand are multiplied and the result is placed in the resultant field of the \nmantissa: {:b}".format(mantissar))
    mantissar >>= 53
    print("Normalizes the mantissa: {:b}".format(mantissar))
    expr = 0
    if mantissar >> 52 == 1:
        expr += 1
        print("The most significant bit of the mantissa is 1. We make an exponential correction.")
    mantissar = str(bin(mantissar))[3:]
    expr += int(exp1, 2) + int(exp2, 2) - 1023
    print("The exponents of the Multiplier (E1) and the multiplicand (E2) bits are added and the base value is subtracted from the added result.\nExponent: {:b}".format(expr))
    print("Final result: {} {:b} {}".format(signr, expr, mantissar))
    return binaryToFloat("{}{:b}{}".format(signr, expr, mantissar))

x1 = -125.125
x2 = 12.0625
print("Rezult: {},\nExpected result: {}".format(floatingMultiplication(x1, x2), x1*x2))