nums_divisible_by_3=[num for num in range(1,100) if num%3==0]
def first_letters_in_a_word(sentence):
    return [word[0] for word in sentence.split(' ')]

nums_and_its_square_tuples=[(num,num**2) for num in range(1,11)]

print(f'Numbers divisible by 3 between 1 and 100 are: {nums_divisible_by_3}')
print(f'First letters in a word: {first_letters_in_a_word("The quick brown fox jumps over the lazy dog")}')
print(f'Numbers and its square: {nums_and_its_square_tuples}')
