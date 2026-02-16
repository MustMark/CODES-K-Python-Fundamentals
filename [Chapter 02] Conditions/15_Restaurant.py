age = int(input())
plate = int(input())

if age >= 60:
    if plate > 1:
        print(f'Pay {plate * 50} baht')
    else:
        print('Free')
else:
    print(f'Pay {plate * 100} baht')