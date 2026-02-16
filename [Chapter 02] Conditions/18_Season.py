month = int(input())
day = int(input())

if month % 3 == 0:
    if month == 3:
        if day < 21:
            print('Winter')
        else:
            print('Spring')
    elif month == 6:
        if day < 21:
            print('Spring')
        else:
            print('Summer')
    elif month == 9:
        if day < 21:
            print('Summer')
        else:
            print('Fall')
    else:
        if day < 21:
            print('Fall')
        else:
            print('Winter')
else:
    if month < 3:
        print('Winter')
    elif month < 6:
        print('Spring')
    elif month < 9:
        print('Summer')
    else:
        print('Fall')