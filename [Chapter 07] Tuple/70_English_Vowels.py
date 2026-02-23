vowels = ('A','E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')

inp = input()

count = 0

for i in inp:
    if i in vowels:
        count += 1

print(count)