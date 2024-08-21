n = int(input())
strings = []
for _ in range(n):
    _ = int(input())
    string = input().lower()
    distinct_chars = []
    seen_chars = set()
    for char in string:
        if char.isalpha() and char not in seen_chars:
            distinct_chars.append(char)
            seen_chars.add(char)
    strings.append(distinct_chars) 
[print("YES" if ''.join(chars) == "meow" else "NO") for chars in strings]