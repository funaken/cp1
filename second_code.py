
class SimpleBars(list):
    def __init__(self, lst):
        list.__init__(self, lst)

    def __str__(self):
        return ''.join(self)

    def next(self):
        lst = list(self)
        for i in range(len(self)):
            cc = self[i]
            cb = self[i - 1] if i != 0 else self[len(self)-1]
            cn = self[i + 1] if i != len(self) - 1 else self[0]
            if   cb == "i" and cc == "T" and cn == "i": lst[i] = "i" 
            elif cb == "i" and cc == "T": lst[i] = " " 
            elif cc == "T" and cn == "i": lst[i] = " "
            elif cc == "T": lst[i] = "i" 
            elif cb == "i" and cc == " " and cn == "i": lst[i] = " "
            elif cb == "i" and cc == " ": lst[i] = "i"
            elif cc == " " and cn == "i": lst[i] = "i"
            elif cc == " ": lst[i] = " "
            elif cc == "i": lst[i] = "T"
            else:
                print("err:" + str(cc) + ":" + str(cb) + ":" + str(cn))
        for i in range(len(self)):
            self[i] = lst[i]
        return str(self)

class Bars(list):
    def __init__(self, lst):
        list.__init__(self, lst)

    def __str__(self):
        return ''.join(self)

    def next(self):
        lst = list(self)
        for i in range(len(self)):
            cc = self[i]
            cb = self[i - 1] if i != 0 else self[len(self)-1]
            cn = self[i + 1] if i != len(self) - 1 else self[0]
            table = [{ " ":" ", "i":"T", "T":"i", "I":"I" }, { " ":"i", "i":"I", "T":" ", "I":"T" }]
            count = 0
            if is_black(cb): count += 1
            if is_black(cn): count += 1
            lst[i] = table[count%2][cc]
        for i in range(len(self)):
            self[i] = lst[i]
        return str(self)

def is_black(c):
    return c == "i" or c == "I"

