num = float(input())

count = 0
while num >= 0.01:
    num = num*3/5
    count += 1

print(count-1)