num = int(input())
temp = []

for i in range(num):
    temp.append(input())

data = input()

while data in temp:
    temp.remove(data)

print(temp)