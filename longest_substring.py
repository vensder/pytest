#!/usr/bin/env python3

# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#
# Longest substring in alphabetical order is: abc


s = 'zyxwvutsrqponmlkjihgfedcba'

long_substring = s[0]
substrings_list = list()
max_len = 0

for i in range(len(s) - 1):
    if s[i+1] >= s[i]:
        long_substring += s[i+1]
    else:
        substrings_list.append(long_substring)
        long_substring = s[i+1]

substrings_list.append(long_substring)

for ss in substrings_list:
    if len(ss) > max_len:
        max_len = len(ss)
        long_substring = ss

print(substrings_list)
print(long_substring)
