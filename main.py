def main():
    n = 1000
    print("Hey - your input is:", n)
    print("Hmm.. I'm doing more stuff with:", n)
    print("And more:", n)

    i = 1
    while i < n:
        print("Hey - I'm busy looking at:", i)
        i *= 2

    for i in range(1, n + 1):
        j = 1
        while j < n:
            print("Hey - I'm busy looking at:", i, "and", j)
            j *= 2


def prefix_average1(x):
    n = len(x)
    a = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += x[i]
        a[j] = total / (j + 1)
    return a


def prefix_average2(x):
    n = len(x)
    a = [0] * n
    total = 0
    for j in range(n):
        total += x[j]
        a[j] = total / (j + 1)
    return a


if __name__ == "__main__":
    main()
