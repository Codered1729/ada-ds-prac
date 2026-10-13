n = int(input("enter the number of jobs\n"))

jobs = []
print("enter job id, deadline, and profit for each job:")
for i in range(n):
    jobid, deadline, profit = map(int, input().split())
    jobs.append([jobid, deadline, profit])

jobs.sort(key=lambda x: x[2], reverse=True)

maxdeadline = max(job[1] for job in jobs)

slot = [-1] * (maxdeadline + 1)
totalprofit = 0

for jobid, deadline, profit in jobs:
    for j in range(deadline, 0, -1):
        if slot[j] == -1:
            slot[j] = jobid
            totalprofit += profit
            break

print("Selected Jobs:")
for j in range(1, maxdeadline + 1):
    if slot[j] != -1:
        print(slot[j], end=" ")
print()
print("Total Profit:", totalprofit)
