num = int(input())
price = num * 100

if price >= 2500:
    num += 4
    price -= 200
elif price >= 2000:
    num += 1
    price -= 150
elif price >= 1000:
    price -= 50

print(num)
print(price)