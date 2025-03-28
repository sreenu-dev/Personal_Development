def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

input_num = int(input("Enter a number: "))
if is_prime(input_num):
    print(f'{input_num} is a prime number')
else:
    print(f'{input_num} is not a prime number')