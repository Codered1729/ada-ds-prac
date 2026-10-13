def merge(a, left, mid, right):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1

    while i <= mid:
        temp.append(a[i])
        i += 1

    while j <= right:
        temp.append(a[j])
        j += 1

    for p in range(len(temp)):
        a[left + p] = temp[p]


def mergesort(a, left, right):
    if left < right:
        mid = (left + right) // 2
        mergesort(a, left, mid)
        mergesort(a, mid + 1, right)
        merge(a, left, mid, right)


n = int(input("enter the number of elements\n"))
print("enter the elements:")

a = []
while len(a) < n:
    a.extend(map(int, input().split()))

mergesort(a, 0, n - 1)

for x in a:
    print(x, end=" ")
print()