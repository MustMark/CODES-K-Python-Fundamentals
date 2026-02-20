num = int(input())
data = int(input())

temp = []

for i in range(num):
    temp.append(int(input()))

print(temp.count(data))