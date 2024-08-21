n = int(input())
count = 0
for _ in range(n):
    lst = [int(x) for x in input().split()]
    if lst.count(1) >= 2:
        count += 1
print(count)
