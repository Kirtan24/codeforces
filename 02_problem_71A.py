def abbreviate(word):
    return print(word) if len(word) <= 10 else print(f"{word[0]}{len(word)-2}{word[len(word)-1]}")
    
n = int(input())
word = []
for i in range(n):
    w = input()
    word.append(w)
for i in range(n):
    abbreviate(word[i])