num = int(input())
temp = []

for i in range(num):
    temp.append(input())

for i in range(num-1, -1, -1):
    print(temp[i])