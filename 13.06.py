'''
def strcounter(s):
    for sym in set(s):
        counter = 0
        for sum_sub in s:
            if sym == sum_sub:
                counter += 1
        print(sym, counter)

strcounter('aaabcd')
'''

def strcounter(s):
    syms_counter = { }
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, count)

strcounter("aaffgggg")
