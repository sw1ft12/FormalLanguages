from RegExpClass import *


def main(regexp, letter, k):
    r = RegExp(regexp, letter, k)
    if(r.parse()):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main(input(), input(), int(input()))
