text = input()
star = 0
noise = 0
for i in text:
    if i == '#':
        noise += 1
    elif i == '*':
        star += 1

print(f'Star: {star}')
print(f'Noise: {noise}')
print('*' * star)