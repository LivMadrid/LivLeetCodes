# abbcccb, k=3 => abbb => a
# returns a string
# word <= len(lst)
    
# stdin =  aba k=2   stdout = aba
#    baac k=2     bc
#
# Complete the 'compressWord' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING word
#  2. INTEGER k
#
    # #"a b b c c c b"
    #  0 1 2 3 4 5 6
def compressWord(word, k):
    # Write your code here
    #base case 
    #range len(string) to find index/ letter i 
    #check to see if i == i if so remove k times 
    #repeat if necessary - maybe recursion is the way to go?
    #return final word 

    
    counter_letter = 1
    
    
    newword = []
    
    
    for idx, letter in enumerate(word):
        if idx < len(word) - 1:
            #if counter_letter ==  k:
            
            print("idx: ", idx, "letter: ", letter)
            print("idx: ", idx+1, "letter: ", word[idx+1])
            print("---------------------------")
            
            if letter == word[idx + 1]:
                counter_letter  += 1
                print(counter_letter)
                if counter_letter == k:
                # list slice or something
                # word[3:6] = "ccc"
                # beg of list slice: idx - counter_lettter + 1
                # end of list slice: idx + 1
                # if word[idx + 1 ]  => then we slice and remove
                
                    if word[idx + 1]:
                        beg_idx = idx - counter_letter + 2
                        end_idx = idx + 2
                        tbs  = word[(beg_idx):end_idx] #O(m)
                        print(tbs)
                        word = word[:beg_idx] + word[end_idx:]
                        print("final word: ", word)
                        if len(word) < k:
                            print("???" , word)
                            return  word
                        else:
                            compressWord(word, k)
            else:
                counter_letter = 1
    return word
           

print("this was returned" , compressWord("aba", 5))

   
    
        
        
        
        
#pseudocode:
# need a counter to check k against how many letters we have
# check to see if that counter ever gets to k
# somehow keep track of the current word and what we've taken
# keep track of repeated characters we took away
# 

# Write a function that takes a list of integers as an argument.
# The function should return a single integer that represents the
# sum of any numbers in the arg list that are followed by
# the same number. Here are some examples:


# [4, 3, 4, 4, 3, 5, 5]
# -> 9

# [4, 4, 4, 5]
# -> 8

# [5, 4, 3]
# -> 0   

# for idx, num in enumerate(nums)  
#iterate through list checking both element, num  - if they are same as next num
# if they are the same --> variable result = [] append to the vairable or list
# add the new list of nums together to find sum

result = []

def same_num_sum(nums):
    for idx, num in enumerate(nums):
        if idx == len(nums)-1: 
            break 
        if num == nums[idx + 1]:
            result.append(num)
            sum_result = sum(result)  
            print(sum_result)
    
            
#same_num_sum([4, 3, 4, 4, 3, 5, 5]) #len(nums)  = 7

    
    
    
    
    
    
    