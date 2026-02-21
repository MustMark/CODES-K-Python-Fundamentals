text = input()

for i, c in enumerate(text):
    if c.islower():
        print(c.upper(), end='')
    else:
        print(c.lower(), end='')