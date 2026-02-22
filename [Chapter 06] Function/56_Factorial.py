def my_factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * my_factorial(num-1)
    
num = int(input())

print(my_factorial(num))