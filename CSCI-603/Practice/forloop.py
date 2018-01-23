

def add(a, b, s):
    while a <b :
        s += a
        a = a + 1
    return s

if __name__ == '__main__':
    print(add(1, 3, 1))