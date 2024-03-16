'''
Reverse a String: Write a function that takes a string as input and returns the string reversed. 
For example, if the input is "hello", the output should be "olleh".

reverse_string_approach_1(any)  -> None (display)
reverse_string_approach_2(any)  -> None (display)
'''
def reverse_of_string(string):
  return string[::-1]
string=input("enter the string to be reversed: ")
print(f'reverse of string is:{reverse_of_string(string)}')
'''
approach 1 using loop
approach 2 not using loop (look up from internet)


Count Vowels in a String: Write a function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string. 
For example, if the input is "hello", the output should be 2.
using loop

Check Palindrome: Write a function that checks if a given string is a palindrome. 
A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward. 
For example, "radar" is a palindrome.

String Anagrams: Write a function that checks if two strings are anagrams of each other. 
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once. 
For example, "listen" and "silent" are anagrams.


#Optional Try your best
Longest Substring Without Repeating Characters: Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating characters in "abcabcbb" is "abc", 
which has a length of 3.
'''
