import random
import string


def random_string(minlen=1, maxlen=256, spaces=True, whitespases=False, enter=False, cyr=False):
    length = random.randint(minlen, maxlen)
    symbols = string.ascii_letters + string.digits + string.punctuation
    if spaces:
        symbols += ' ' * 10
    if whitespases:
        symbols += string.whitespace[:-2] * 3
    if enter:
        symbols += "\n"*4
    if cyr:
        cyr_symbol = ''.join([chr(l) for l in range(0x0400, 0x0450)
                              if chr(l).isprintable()])
        symbols += cyr_symbol
    result = ''.join(random.choices(symbols, k=length))
    return result
