
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here

    if n % 3 != 0 and n % 5 != 0:
        print (n)
    #if i is a multiple of 3 and 5 print FizzBuzz
    if n % 3 == 0 and n % 5 == 0:
        print ("FizzBuzz")
    #if i is a  multiple of 3 (not 5) print Fizz
    if n % 3 == 0  and  n % 5 != 0:
        print("Fizz")
    #if i is a multiple of 5 (not 3) print Buzz
    if n % 3 != 0 and  n % 5 == 0:
        print("Buzz")
    #if i is not a multiple of 3 or 5 print i 
    else:
        return


fizzBuzz(