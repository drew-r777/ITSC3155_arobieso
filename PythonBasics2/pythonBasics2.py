# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

# Return multiple of 3 that occurs most in a string
def count_threes(n):
    # YOUR CODE HERE
    d = dict = {
        "3": 0,
        "6": 0,
        "9": 0
    }
    for i in n:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1

    if d["6"] > d["3"] and d["6"] > d["9"]:
        return 6
    elif d["9"] > d["3"] and d["9"] > d["6"]:
        return 9
    else:
        return 3

# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.

# Return longest repeating characters
def longest_consecutive_repeating_char(s):
    # YOUR CODE HERE
    dictCurr = {}
    dictHighest = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    for i in range(0, len(s)):
        # if values are equal
        if i == len(s) - 1:
            # handle reaching end of string
            continue
        if s[i] == s[i + 1]:
            # if not in dictionary, then add it
            if s[i] not in dictCurr:
                dictCurr[s[i]] = 1
            # else increment value
            else:
                dictCurr[s[i]] += 1
            # if curr value has surpassed highest chain value, assign new value to highest
            if dictHighest.get(s[i]) < dictCurr.get(s[i]):
                dictHighest[s[i]] = dictCurr.get(s[i])
        # Values unequal, clear current
        else:
            dictCurr.clear()
    # loop through dictHighest and find the largest values
    largest = 0
    arr = []
    # Find the largest value
    for value in list(dictHighest.values()):
        if value > largest:
            largest = value
    # Add all keys with largest value to arr
    for key in list(dictHighest.keys()):
        if dictHighest[key] == largest:
            arr.append(key)
    return arr


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
    # YOUR CODE HERE
    s = s.lower()
    s = s.replace(" ", "")
    # print(s)
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
