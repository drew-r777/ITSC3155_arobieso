# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  # YOUR CODE HERE
    count = 0
    if n < 3:
        return 0
    for i in range(0, n):
        if i % 3 == 0:
            count = count + 1
    return count


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE
    character = ''
    count = 0
    for i in range(0, len(s)):
        current = 1
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                current = current + 1
            else:
                break
        if current > count:
            count = current
            character = s[i]
    return character


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
    #print(s)
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True