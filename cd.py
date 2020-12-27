import sys


def cd_case(input, n, m):
    jack = set(int(input.readline()) for _ in range(n))
    rv = 0
    for _ in range(m):
        if int(input.readline()) in jack:
            rv += 1
    return rv


def cd(input):
    while True:
        n, m = map(int, input.readline().split())
        if n == 0 and m == 0:
            break
        yield cd_case(input, n, m)


def main(input):
    for rv in cd(input):
        print(rv)


if __name__ == '__main__':
    main(sys.stdin)