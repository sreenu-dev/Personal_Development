def odd_or_even(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
input_num=int(input("Enter a number: "))
print(odd_or_even(input_num))