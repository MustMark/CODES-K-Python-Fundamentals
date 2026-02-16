most = 0
most_index = 0

num = int(input())
if num > most:
    most = num
    most_index = 1
num = int(input())
if num > most:
    most = num
    most_index = 2
num = int(input())
if num > most:
    most = num
    most_index = 3
num = int(input())
if num > most:
    most = num
    most_index = 4
num = int(input())
if num > most:
    most = num
    most_index = 5

print(most_index)