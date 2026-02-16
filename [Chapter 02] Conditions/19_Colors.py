colors = ['Red', 'Yellow', 'Blue']

first = input()
second = input()

if first in colors and second in colors:
    color = first + second
    if colors[0] in color and colors[1] in color:
        print('Orange')
    elif colors[0] in color and colors[2] in color: 
        print('Violet')
    else:
        print('Green')
else:
    print('Error')