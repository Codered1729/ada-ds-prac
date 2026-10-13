def printtree(root, keys, i, j, prefix, label):
    if i > j:
        return

    r = root[i][j]
    print(prefix + label + str(keys[r]))

    printtree(root, keys, i, r - 1, prefix + "    ", "Left: ")
    printtree(root, keys, r + 1, j, prefix + "    ", "Right: ")


n = int(input("Enter number of keys\n"))

print("Enter sorted keys")
keys = []
while len(keys) < n:
    keys.extend(map(int, input().split()))

print("Enter search frequencies")
freq = []
while len(freq) < n:
    freq.extend(map(int, input().split()))

dp = [[0] * n for i in range(n)]
root = [[0] * n for i in range(n)]
prefixsum = [0] * (n + 1)

for i in range(n):
    prefixsum[i + 1] = prefixsum[i] + freq[i]
    dp[i][i] = freq[i]
    root[i][i] = i

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        total = prefixsum[j + 1] - prefixsum[i]
        dp[i][j] = float('inf')

        for r in range(i, j + 1):
            left = dp[i][r - 1] if r > i else 0
            right = dp[r + 1][j] if r < j else 0
            cost = left + right + total

            if cost < dp[i][j]:
                dp[i][j] = cost
                root[i][j] = r

print("Minimum search cost:", 0 if n == 0 else dp[0][n - 1])

if n > 0:
    print("OBST structure:")
    printtree(root, keys, 0, n - 1, "", "Root: ")

