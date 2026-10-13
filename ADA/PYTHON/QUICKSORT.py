def partition(a, left, right):
    i = left - 1
    pivot = a[right]

    for j in range(left, right):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    i += 1
    a[i], a[right] = a[right], a[i]
    return i


def quicksort(a, left, right):
    if left < right:
        pivot = partition(a, left, right)
        quicksort(a, left, pivot - 1)
        quicksort(a, pivot + 1, right)


n = int(input("enter the number of elements\n"))
print("enter the elements:")

a = []
while len(a) < n:
    a.extend(map(int, input().split()))

quicksort(a, 0, n - 1)

for x in a:
    print(x, end=" ")
print()

