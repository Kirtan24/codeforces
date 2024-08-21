n=int(input())
x=0
for _ in range(n):
    operation = input().strip()
    if operation in ['++X', 'X++']:
        x += 1
    elif operation in ['--X', 'X--']:
        x -= 1
print(x)