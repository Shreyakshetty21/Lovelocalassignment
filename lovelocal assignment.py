#       EASY 1
#Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal 
#substring consisting of non-space characters only.


def length_of_last(s):              #Function definition
    wd = s.split()                  #The split() method is used to split the input string s into a list of words. 
    if not wd:                      #This condition checks if the list of wd (words) is empty. If it is, the function returns 0.
        return 0
    return len(wd[-1])              #This line returns the length of the last word in the list.
input = "fly me to the moon  "      #Here, the function is called with the example input " fly me to the moon ". The result is the length of the last word, which is "moon" with a length of 4.
res = length_of_last(input)   
print(res)                          #Prints the result as 4


#************************************************************************************************************************************************************************************************************************************#


#         MEDIUM 2
#Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.


def maj(nums):                      #Function definition
    cand1, cand2 = None, None       # Initialize candidates and counters candidate1 and candidate2 represent the two potential majority candidates.
    count1, count2 = 0, 0           #count1 and count2 represent the counters for the corresponding candidates.
                       
                                        
    for num in nums:                #The code iterates through the array (nums).
        if num == cand1:            #If the counts are 0, the current number becomes a new candidate with a count of 1.                              
            count1 += 1             #If the counts are not 0, decrement both counts (a form of "cancellation").
        elif num == cand2:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = num, 1
        elif count2 == 0:
            cand2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    count1, count2 = 0, 0             #Reset counters and iterate through the array again to count occurrences of each candidate.
    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1

    result = []
    if count1 > len(nums) // 3:        #Check if the counts of candidates exceed ⌊ n/3 ⌋, and if so, add them to the result list.
        result.append(cand1)
    if count2 > len(nums) // 3:
        result.append(cand2)

    return result

nums = [3, 2, 3]                       #For the input [3, 2, 3], the output will be [3], indicating that 3 is the element appearing more than ⌊ n/3 ⌋ times in the array.
res = maj(nums)
print(res)


#*******************************************************************************************************************************************************************************************************************************************************************************#

#         HARD 2
#You are given a string s. You can convert s to a 
#palindrome by adding characters in front of it.
#Return the shortest palindrome you can find by performing this transformation.

def short_pal(s):                           #Function definition
    
    def pal_prefix(s):                      #This function takes a string s as input.
        i = len(s)                          #It initializes an index i to the length of the string.
        while i > 0 and s != s[::-1][:i]:   #It enters a loop that continues as long as i is greater than 0 and the substring s is not a palindrome.
            i -= 1                          #In each iteration, it decrements i.
        return s[i:][::-1]                  #The function returns the longest palindrome prefix found by reversing the characters from index i onward.

    pal_prefix = pal_prefix(s)              #This line finds longest palindrome

    result = s[len(pal_prefix):][::-1] + s

    return result                           #Returns result

s = "aacecaaa"
res = short_pal(s)
print(res)                                  #print result


                             
                              


