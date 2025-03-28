def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

input_num=int(input("Enter a number: "))
print(f'The factorial of {input_num} is {factorial(input_num)}')