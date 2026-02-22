my_list = [1, 3, 7, 41]

def double_it(data):
    for i in range(len(data)):
        data[i] = data[i] * 2

double_it(my_list)
print(my_list)