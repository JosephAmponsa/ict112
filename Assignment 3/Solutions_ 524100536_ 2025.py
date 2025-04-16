"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original = "programming"
reversed_str = original[::-1]
print(reversed_str)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter your full name: ")
name = full_name.split()
initials = [name[0].upper() for name in names]
print(".". join(initials) + ".")


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    s = s.lower().replace("", "") # make case-insessitive and ignore spaces
    return s == s[::-1]

test_string = input("Enter a string check for palindrome: ")
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome")
else:
    print(f"'{test_string}' is not a palindrome")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"The sentence contains {len(words)} words.")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_string = "this is a string and is an example."
modified_string = original_string.replace("is", "was")
print(modified_string)