num = int(input())

temp = []

for i in range(num):
    temp.append(int(input()))

temp.sort()

for i in temp:
    print(i)