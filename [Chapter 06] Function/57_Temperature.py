def to_fahrenheit(celsius):
    return celsius/5*9+32

def to_kelvin(celsius):
    return celsius+273

def to_reaumur(celsius):
    return celsius/5*4

in_celsius = float(input())
to_unit = input()
if to_unit == "F":
    print(to_fahrenheit(in_celsius), 'Fahrenheit')
elif to_unit == "K":
    print(to_kelvin(in_celsius), 'Kelvin')
elif to_unit == "R":
    print(to_reaumur(in_celsius), 'Reaumur')