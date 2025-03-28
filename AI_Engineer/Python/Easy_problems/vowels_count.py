def count_vowels(s):
    vowels = 'aeiou'
    return sum([1 for i in s if i in vowels])

s = input("Enter a string: ")
print(f'The number of vowels in {s} is {count_vowels(s)}')