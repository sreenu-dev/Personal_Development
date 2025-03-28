def remove_duplicats(list_data):
    d=[]
    outi=[d.append(data) for data in list_data if data not in d]
    return d

input_list=[int(x) for x in input("Enter numbers giving space").split(' ')]
print(f'Refined data of {input_list} after removing duplicates are {remove_duplicats(input_list)}')