def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")
if is_anagram(input_str1, input_str2):
    print(f'{input_str1} and {input_str2} are anagrams')
else:
    print(f'{input_str1} and {input_str2} are not anagrams')