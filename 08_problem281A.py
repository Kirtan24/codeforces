w = input()
c = ord(w[0])
if 'a' <= w[0] <= 'z':
    first_char = chr(ord(w[0]) - 32)
    w = first_char + w[1:]
print(w)