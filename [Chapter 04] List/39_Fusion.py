cat_list = ['Siamese', 'Persian', 'Korat']
temp = []

for i in range(3):
    temp.append(input())

temp.extend(cat_list)

print(temp)