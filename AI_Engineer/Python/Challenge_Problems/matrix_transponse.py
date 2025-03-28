def matrix_transponse(matrix_input):
    new_transposed_matrix=[]
    for i in range(len(matrix_input[0])):
        new_subList=[]
        for j in range(len(matrix_input)):
            print(f'{j}:{i}',end=" ")
            print(matrix_input[j][i])
            new_subList.append(matrix_input[j][i])
        new_transposed_matrix.append(new_subList)
        print("")
    return new_transposed_matrix
input_static=[[1,2,3],[4,5,6]]
print(f'New Transponsed Matrix:{matrix_transponse(input_static)}')