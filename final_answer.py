
from first_code  import lets_take_tea_break
from second_code import Bars
from third_code  import encode_morse
import string

chars = " iTI"
final_hash = 1758412232636122750
final_str = 1758412232636122750

def bars_num_to_str(num):
    l = []
    while num:
        x = num % 4
        l.append(chars[x])
        num /= 4
    l.reverse()
    s = ''.join(l)
    while len(s) < 32:
        s = ' ' + s
    return s

def reverse_str(s):
    return s[::-1]

def check_answer(answer):
    bars = Bars(" "*32)
    bars_pos = 0
    for c in answer:
        c = c.upper()
        assert(ord(' ') < ord(c) and ord(c) < 127)
        code = encode_morse(c)
        for i in code:
            bars.xor(bars_pos, i)
            bars_pos += 1; bars_pos %= len(bars)
        bars_pos += 1; bars_pos %= len(bars)
        bars.next()
    hash_value = bars.num()
    if True:
        s = bars_num_to_str(hash_value)
        ans = "iT iTiI T"
        if 0 <= s.find(ans):
            print('anser='.join(answer))
    return hash_value == 1758412232636122750

def simple_check(answer):
    chk_str = "iTiIIT"
    bars = Bars(" "*32)
    bars_pos = 0
    count = 0
    for c in answer:
        c = c.upper()
        assert(ord(' ') < ord(c) and ord(c) < 127)
        code = encode_morse(c)
        for i in code:
            bars.xor(bars_pos, i)
            bars_pos += 1; bars_pos %= len(bars)
        bars_pos += 1; bars_pos %= len(bars)
        bars.next()
    #print("answer={0} bars={1} bars_str={2}".format(''.join(answer), str(bars), str(bars)[len(bars)-len(answer):]))
    return chk_str[0:len(answer)] == str(bars)[len(bars)-len(answer):]

def solve_with_backtracking(answer, depth):
    print("solve_with_backtracking({0},{1})".format(''.join(answer), str(depth)))
    if depth == 1:
        for c in string.ascii_uppercase:
            new_answer = list(answer)
            new_answer.append(c)
            if check_answer(new_answer):
                print("answer=" + str(new_answer))
                return True
        return False
    for i in range(depth):
        for c in string.ascii_uppercase:
            tmp_answer = list(answer)
            tmp_answer.append(c)
            bars = Bars(tmp_answer)
            if simple_check(tmp_answer) == False:
                continue
            elif solve_with_backtracking(tmp_answer, depth - 1):
                return True
    return False

def print_hash():
    s = bars_num_to_str(final_hash)
    print("final_hash:{0} bars.str:'{1}'".format(final_hash, s))

def solve():
    answer = []
    for depth in range(1, 10):
        print("depth=" + str(depth))
        if solve_with_backtracking(answer, depth):
            return

def solve2():
    h = 1758412232636122750
    s = bars_num_to_str(h)
    print("bars.str:" + s)
    barsd = Bars(s)
    bars = Bars(' ' + str(barsd))
    print("bars.num:" + str(bars.num()))
    bars_len = len(bars)
    print("bars.len=" + str(bars_len))
    bars_pos = bars_len - 1
    answer = []
    while 0 <= bars_pos:
        found = False
        for c in string.ascii_uppercase:
            tmp_bars = Bars(bars)
            tmp_bars.prev()
            tmp_pos = bars_pos
            code = encode_morse(c)
            rcode = reverse_str(code)
            ok = 0
            for i in rcode:
                tmp_bars.xor(tmp_pos, i)
                if tmp_bars[tmp_pos] != ' ':
                    ok += 1
                tmp_pos -= 1; tmp_pos %= bars_len
            if len(code) - 1 <= ok:
                found = True
                bars.prev()
                #print("c=" + c)
                answer.append(c)
                for i in rcode:
                    bars.xor(bars_pos, i)
                    bars_pos -= 1; bars_pos %= bars_len
                break
        if found == False:
            print("failed")
            break
    print("bars=" + str(bars))

def solve3():
    e = 65537
    n = 47775743999999999999 # TODO: this bit length is too short for RSA!
    h = 1758412232636122750
    signature = 26984024434151540355
    bars = Bars(" "*32)
    bars_pos = 0
    data = "EBMDKA"
    for c in data:
        c = c.upper()
        print("c=" + c)
        assert(ord(' ') < ord(c) and ord(c) < 127)
        code = encode_morse(c)
        for i in code:
            bars.xor(bars_pos, i)
            bars_pos += 1; bars_pos %= len(bars)
        bars_pos += 1; bars_pos %= len(bars)
        print(bars)
        bars.next()
        print(bars)
    hash_value = bars.num()
    return lets_take_tea_break(hash_value, e, n, signature)

def solve4():
    answer = []
    solve_with_backtracking(answer, 4)

def solve5(answer, depth):
    if depth == 0:
        print("anser={0}".format(''.join(answer)))
        return False
    for i in range(depth):
        for c in string.ascii_uppercase:
            tmp_answer = list(answer)
            tmp_answer.append(c)
            bars = Bars(tmp_answer)
            if simple_check(tmp_answer) == False:
                continue
            elif solve5(tmp_answer, depth - 1):
                return True
    return False

if __name__ == "__main__":
    print_hash()
    #solve5([], 3)
    solve3()

