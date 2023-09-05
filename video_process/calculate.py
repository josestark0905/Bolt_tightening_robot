import math


def ans(n):
    res = 0
    if n > 10:
        while n > 10:
            n = n / 10
            res += 1
        print(n, res)
    if n < 1:
        while n < 1:
            n *= 10
            res -= 1
        print(n, res)


if __name__ == "__main__":
    print(0.0259*math.log(0.00001, math.e))
