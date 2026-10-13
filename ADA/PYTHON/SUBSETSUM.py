def subsetsum(arr, n, total, sol):
    if total == 0:
        print(sol)
        return

    if n == 0 or total < 0:
        return

    sol[n - 1] = 1
    subsetsum(arr, n - 1, total - arr[n - 1], sol)

    sol[n - 1] = 0
    subsetsum(arr, n - 1, total, sol)


n = int(input())
print("Enter array elements:")
arr = []
while len(arr) < n:
    arr.extend(map(int, input().split()))

print("Enter Sum(k):")
k = int(input())

sol = [0] * n
subsetsum(arr, n, k, sol)

