
def decode_morse(str):
    words = str.rsplit('\n', 1)[0].split()
    lst = list()
    for c in words:
        lst.append(decode(c))
    return ''.join(lst)

def decode(c):
    if c == "iI": return "A"
    elif c == "Iiii": return "B"
    elif c == "IiIi": return "C"
    elif c == "Iii": return "D"
    elif c == "i": return "E"
    elif c == "iiIi": return "F"
    elif c == "IIi": return "G"
    elif c == "iiii": return "H"
    elif c == "ii": return "I"
    elif c == "iIII": return "J"
    elif c == "IiI": return "K"
    elif c == "iIii": return "L"
    elif c == "II": return "M"
    elif c == "Ii": return "N"
    elif c == "III": return "O"
    elif c == "iIIi": return "P"
    elif c == "IIiI": return "Q"
    elif c == "iIi": return "R"
    elif c == "iii": return "S"
    elif c == "I": return "T"
    elif c == "iiI": return "U"
    elif c == "iiiI": return "V"
    elif c == "iII": return "W"
    elif c == "IiiI": return "X"
    elif c == "IiII": return "Y"
    elif c == "IIii": return "Z"
    else: return "@"

