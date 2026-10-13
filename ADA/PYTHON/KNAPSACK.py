n = int(input("enter number of items: "))
items = []

for i in range(n):
    print(f"enter item {i + 1} weight and profit:")
    w, p = map(int, input().split())
    items.append([w, p, p / w])

items.sort(key=lambda x: x[2], reverse=True)

capacity = int(input("enter max capacity: "))
maxprofit = 0.0
i = 0

while capacity > 0 and i < n:
    weight = items[i][0]
    profit = items[i][1]
    ratio = items[i][2]

    if weight <= capacity:
        capacity -= weight
        maxprofit += profit
    else:
        take = capacity * ratio
        maxprofit += take
        capacity = 0
    i += 1

print("maxprofit :", maxprofit)
