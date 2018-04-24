def multiplying(multiplicand, multiplier):
    product = 0
    expectresult = multiplicand*multiplier
    lengthofprod = multiplicand.bit_length() + multiplier.bit_length()
    print("Multiplicand: {:b}\nMultiplier: {:b}\nProduct: {}".format(multiplicand, multiplier, format(product, '0' + str(lengthofprod) + 'b')))
    print("===================================")
    for i in range(multiplier.bit_length()):
        if multiplier & 1:
            print("last bit of multiplier is 1 so add multiplicand to product")
            product += multiplicand
        print("shift multiplicand left by 1")
        multiplicand <<= 1
        print("shift multiplier right by 1")
        multiplier >>= 1
        print("Multiplicand: {:b}\nMultiplier: {:b}\nProduct: {}".format(multiplicand, multiplier,
                                                                         format(product, '0' + str(lengthofprod) + 'b')))
        print("===================================")
    print("Result: {}, expected result: {}".format(product, expectresult))
    return product

multiplying(9,13)