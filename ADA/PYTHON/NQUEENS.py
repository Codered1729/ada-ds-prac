def place(k, i, x):
    for j in range(1, k):
        if x[j] == i:
            return False
        if abs(x[j] - i) == abs(j - k):
            return False
    return True


def nqueen(k, n, x):
    for i in range(1, n + 1):
        if place(k, i, x):
            x[k] = i
            if k == n:
                for j in range(1, n + 1):
                    print(x[j], end=" ")
                print()
            else:
                nqueen(k + 1, n, x)


n = int(input("Enter n: "))

if n < 4:
    print("-1")
else:
    x = [0] * (n + 1)
    print("The possible ways are:")
    nqueen(1, n, x)

