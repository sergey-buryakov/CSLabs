remainderPart = 0b0111111111111111111111111111111100000000000000000000000000000000
quotientPart = 0b0000000000000000000000000000000011111111111111111111111111111111

def Division(dividend, divisor):
    register = 0b0000000000000000000000000000000000000000000000000000000000000000
    register += dividend
    print("Initial register: {:065b}".format(register))
    for i in range(32):
        register <<= 1
        print("Shifted register to the left")
        print("register: {:065b}".format(register))

        remainder = (register & remainderPart) >> 32
        print("Register > 0 then subtract divisor")
        remainder = remainder - divisor

        if (remainder >= 0):
            print("Remainder > 0 then add to register 1")
            register &= quotientPart
            register |= remainder << 32
            register += 1

        print("register: {:065b}".format(register))
        print("remainder: {:032b}".format(register >> 32))
        print("quotient: {:032b}".format(register & quotientPart))
        print("=================")
    return register

res = Division(17, 4)
print("quotient: {}, remainder: {}".format(res & quotientPart, res >> 32))
