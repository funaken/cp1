
morse_codes = [
    "iI",
    "Iiii",
    "IiIi",
    "Iii",
    "i",
    "iiIi",
    "IIi",
    "iiii",
    "ii",
    "iIII",
    "IiI",
    "iIii",
    "II",
    "Ii",
    "III",
    "iIIi",
    "IIiI",
    "iIi",
    "iii",
    "I",
    "iiI",
    "iiiI",
    "iII",
    "IiiI",
    "IiII",
    "IIii",
    ]

def decode_morse(str):
    words = str.rsplit('\n', 1)[0].split()
    lst = list()
    for c in words:
        lst.append(decode(c))
    return ''.join(lst)

def decode(c):
    return chr(ord('A') + morse_codes.index(c))

def encode_morse(c):
    return morse_codes[ord(c.upper()) - ord('A')]

