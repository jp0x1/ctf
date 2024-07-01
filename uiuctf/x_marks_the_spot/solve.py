from itertools import cycle

# flag = b'uiuctf{'
f = open('ct', mode='rb')
data = f.read()
print(data)


key = b"hdiqbfj"

parts = [b"a",b"b",b"c",b"d",b"e",b"f",b"g",b"h",b"i",b"j",b"k",b"l",b"m",b'n',b'o',b'p',b'q',b'r',b's',b't',b'u',b'v']


for i in parts:
    flag = bytes(x ^ y for x, y in zip(data, cycle(key+i)))
    if b'uiuctf{' in flag:
        print(flag)

