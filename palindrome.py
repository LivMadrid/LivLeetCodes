# Palindrome Number
# Easy

# 3155

# 1714

# Add to List

# Share
# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

# Example 1:

# Input: x = 121
# Output: true
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Example 4:

# Input: x = -101
# Output: false
 

# # Constraints:

# # -231 <= x <= 231 - 1

# num = 121

# def palindrome(num):
#     if num <= 10:
#         return False

#     stringnum = str(num)
#     print(stringnum)
#     # length = len(stringnum)
   
#     # for i in range(length):
#     #     print(i)
#     if stringnum[::-1] == stringnum:
#         return print(f'{num} is palindrome')
#     else: 
#         return print(f'{num} is not a palindrome')

# palindrome(num)


# 11122111

# 121


#nums that are oddly indexed start at mid point
#nums that are evenly indexed check middle two nums ? then compare indexes outward of both?

#len(x)
x = 1

def count_digits(x):
    digits = 1
    while x % (10 ** digits) != x:
      digits += 1 
    return digits 





def palindrome(x):

    digits = count_digits(x)

    for i in range(digits):
        pos = i + 1
        first = x // (10 ** (digits - pos))
        last = x % (10 ** pos)
        print(x, first, last, pos)
        if first != last:
          return False

        x = (x % (10 ** pos))

    return True
        


        