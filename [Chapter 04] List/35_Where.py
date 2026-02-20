animals = []

for i in range(5):
    animals.append(input())

target = input()

target_index = -1

for i in range(len(animals)):
    if animals[i] == target:
        target_index = i
        break

if target_index >= 0:
    print(target_index)
else:
    print('Error')