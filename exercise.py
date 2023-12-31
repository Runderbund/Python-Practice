# How do you reverse a string?
# How do you determine if a string is a palindrome?
# How do you calculate the number of numerical digits in a string?
# How do you find the count for the occurrence of a particular character in a string?
# How do you find the non-matching characters in a string?
# How do you find out if the two given strings are anagrams?
# How do you calculate the number of vowels and consonants in a string?
# How do you total all of the matching integer elements in an array?
# How do you reverse an array?
# How do you find the maximum element in an array?
# How do you sort an array of integers in ascending order?
# How do you print a Fibonacci sequence using recursion?
# How do you calculate the sum of two integers?
# How do you find the average of numbers in a list?
# How do you check if an integer is even or odd?
# How do you find the middle element of a linked list?
# How do you remove a loop in a linked list?
# How do you merge two sorted linked lists?
# How do you implement binary search to find an element in a sorted array?
# How do you print a binary tree in vertical order?

def string_reverse(string):
    return string[::-1]

def is_palindrome(string):
    return string == string[::-1]

def count_digits(string):
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    return count

def count_char(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

def find_nonmatching_chars(string1, string2):
    nonmatching = []
    for char in string1:
        if char not in string2:
            nonmatching.append(char)
    for char in string2:
        if char not in string1:
            nonmatching.append(char)
    return nonmatching

def determine_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

def count_vowels_consonants(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0
    for char in string:
        if char.lower() in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
    return vowel_count, consonant_count

def sum_matching_integers(array):
    # Totals all integers in an array
    total = 0
    for num in array:
        if isinstance(num, int):
            total += num
    return total

def sum_matching_integers_2(array, int):
    # Totals all integers that match a given value in an array
    total = 0
    for char in array:
        if char == int:
            total += char
    return total

def reverse_array(array):
    new_array = []
    i = len(array) - 1
    while i >=0:
        new_array.append(array[i])
        i -= 1
    return new_array

def reverse_array_2(array):
    new_array = []
    for char in array:
        new_array.insert(0, char)
    return new_array