def find_max_min(input_list):
    max_num = input_list[0]
    min_num = input_list[0]
    for i in input_list:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    return (max_num, min_num)

input_list = [int(i) for i in input("Enter a list of numbers separated by space: ").split()]
print(f'The maximum and minimum numbers in the list are: {find_max_min(input_list)}')