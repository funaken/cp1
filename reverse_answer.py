
from first_code  import lets_take_tea_break
from second_code import Bars
from third_code  import encode_morse
import string


def solve_x(bars, bars_pos, s):
    #if len(s) == 4:
    if False:
        barsp = bars.prev()
        #print("a='{0}'".format(barsp[20:30]))
        if barsp[20:30] == ' '*10:
            print("bars={0} s={1}".format(str(), s))
        return
    bars.prev()
    bars_pos -= 1
    if bars_pos < 0:
        return
    for c in string.ascii_uppercase:
        new_bars = Bars(bars)
        new_bars_pos = bars_pos
        code = encode_morse(c)
        rcode = code[::-1]
        for i in rcode:
            new_bars_pos -= 1
            if new_bars < 0:
                break
            new_bars.xor(new_bars_pos, i)
        #print("{0} c={1}".format(str(new_bars), code))
        #print("bars={0} c={1}".format(str(new_bars), c))
        if new_bars_pos <= 0:
            print("bars={0} s={1}".format(str(new_bars), s))
        else:
            print("new_bars_pos={0} codelen={1}".format(new_bars_pos, len(code)))
            bp = str(new_bars)[new_bars_pos:new_bars_pos+len(code)]
            print("bars='{0}' bp='{1}' c={2}".format(str(new_bars), bp, c + s))
            if bp == ' '*(len(code)):
                solve_x(new_bars, new_bars_pos, c + s)

def solve():
    orig = ' iT iTiI T TTiTIITITIITTi iTiIIT'
    bars = Bars(orig)
    bars_pos = len(orig) - 7
    solve_x(bars, bars_pos, "")
    if False:
        bars.prev()
        print(str(bars))
        for c in string.ascii_uppercase:
            new_bars = Bars(bars)
            bars_pos = len(orig) - 7
            code = encode_morse(c)
            rcode = code[::-1]
            for i in rcode:
                new_bars.xor(bars_pos, i)
                bars_pos -= 1; bars_pos %= len(bars)
            print("new_bars={0} xor={1}".format(str(new_bars), code))
            print("prv_bars={0}".format(str(new_bars.prev())))

if __name__ == "__main__":
    solve()
