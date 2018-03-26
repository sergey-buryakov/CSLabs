import math, re

def ReadFile(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    return text

def FindFrequencyAndNumberChars(text):
    freqChars = {}
    numberOfChars = 0
    for char in text:
        numberOfChars += 1
    for char in text:
        if not char in freqChars:
            freqChars[char] = text.count(char) / numberOfChars
    return freqChars, numberOfChars

def FindAvarangeEntropy(p):
    entropy = 0
    for ch in p:
        entropy -= p[ch] * math.log2(p[ch])
    return entropy

file = "lab1/PCI"

if __name__ == "__main__":
    freqChars, numberOfChars = FindFrequencyAndNumberChars(ReadFile(file))
    entropy = FindAvarangeEntropy(freqChars)
    quantity = FindAvarangeEntropy(freqChars) * numberOfChars / 8
    count = 0
    for key in sorted(freqChars.keys()):
        count += 1
        print("'{0}': {1}".format(key,freqChars[key]))
    print("entropy: {},\tquantity: {} bytes".format(entropy, round(quantity)))


