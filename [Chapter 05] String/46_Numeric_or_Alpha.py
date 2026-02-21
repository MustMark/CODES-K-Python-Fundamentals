text = input()

number = False
alphabet = False

for i in text:
    if i.isnumeric():
        number = True
    elif i.isalpha():
        alphabet = True

if number and alphabet:
    print('Mixed')
elif number:
    print('Number')
else:
    print('Alphabet')