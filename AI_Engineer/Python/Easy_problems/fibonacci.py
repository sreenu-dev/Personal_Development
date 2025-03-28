import sys

def first_n_fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list

input_num=int(input("Enter a number: "))
outi=first_n_fibonacci(input_num)
sys.set_int_max_str_digits(1000000)
for i in range(input_num):
    if(i==0):
        print('[',end='')
    print(outi[i], end=' ')
    if(i==input_num-1):
        print(']')
    else:
        print(',',end=' ')