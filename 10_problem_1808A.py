def largeAndSmallDigit(number):
    number_str = str(number)
    largest_digit = max(number_str)
    smallest_digit = min(number_str)
    return int(largest_digit) - int(smallest_digit)

n = int(input())
new_arr = []
array = [list(map(int, input().split())) for i in range(n)]
for i in range(len(array)):
    for j in range(array[i][0],array[i][1]+1):
        new_arr.append(largeAndSmallDigit(j))
print(new_arr)