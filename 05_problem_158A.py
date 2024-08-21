# n, k = map(int, input().split())
# c=0
# m = [int(_) for _ in input().split()]
# if all(x >= 0 for x in m) and any(x > 0 for x in m):
#     for i in m:
#         if i >= m[k-1]:
#             c+=1
# print(c)


n, k = map(int, input().split())
m = [int(x) for x in input().split()]
c = 0
k_score = m[k - 1]
for score in m:
    if score > 0 and score >= k_score:
        c += 1
print(c)