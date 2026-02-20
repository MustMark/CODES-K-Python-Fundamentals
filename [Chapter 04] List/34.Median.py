num = int(input())

x = []

for i in range(num):
    x.append(float(input()))

x.sort()
mid = int(len(x)/2)

if len(x) % 2 == 0:
    print(float((x[mid-1] + x[mid]) / 2))
else:
    print(float(x[mid]))