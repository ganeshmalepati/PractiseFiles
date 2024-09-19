# def reverseString(s):
#     reverse_s = ""
#     for char in s:
#         reverse_s = char + reverse_s
#     return reverse_s
# s = input("Enter a string: ")
# print(reverseString(s))


# def ReverseBySlice(s):
#     return s[::-1]
# s = input("Enter a string: ")
# print(ReverseBySlice(s))




# def Palindrome(s):
#     s = s.replace(" ", " ").lower()
#     left = 0
#     right = len(s)-1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
# s = input("Enter a string: ")
# print(Palindrome(s))




# def Vowels_in_String(s):
#     vowels = ('aeiouAEIOU')
#     count = 0
#     found_vowels = set()
#     for char in s:
#         if char in vowels:
#             count += 1
#             found_vowels.add(char)
#     return count, found_vowels

# s = input("Enter a string: ")
# print(Vowels_in_String(s))


# def Occurence_of_char(s):
#     new_str = {}
#     for char in s:
#         if char in new_str:
#             new_str[char] += 1
#         else:
#             new_str[char] = 1
#     return new_str
# s = input("Enter a string: ")
# print(Occurence_of_char(s))


# def Frequency_of_each_char(s):
#     char_count = {}
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1

#     most_common_char = max(char_count, key=char_count.get)
#     most_common_count = char_count[most_common_char]
#     return most_common_char, most_common_count
#     pass
# s = input("Enter a string: ")
# print(Frequency_of_each_char(s))


def Remove_Duplicate_result(s):
    seen = set()                  # Here a set is defined and set not allows duplicate values
    result = []                   # the final result is stored here
    for char in s:
        if char not in seen:
            seen.add(char)        # when a char is unique it will store in seen set()
            result.append(char)   # After removing the duplicate values each unique char are stored in result list
    return ''.join(result)        # This will Join all the values
s = input("Enter a string: ")
print(Remove_Duplicate_result(s))

