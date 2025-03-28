def reverse_list_without_reverse(input_list):
    for i in range(len(input_list)//2):
        input_list[i], input_list[-i-1] = input_list[-i-1], input_list[i]
    return input_list