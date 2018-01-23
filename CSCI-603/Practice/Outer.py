def outer(x):
    print("x is " + str(x))
    x = x * 3
    inner(x)
    print("x is " + str(x))

def inner(x):
    print("x is " +str(x))
    x = x*2
    print("x is " + str(x))

def main():
    print("first answer:")
    x = 13
    outer(x)

if __name__ == '__main__':
        main()