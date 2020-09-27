# Consider the following:

# A string S, , of lengthn  where .
# An integer k, , where k is a factor of n.
# We can split s  into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

# The characters in ui are a subsequence of the characters in ti.
# Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
# Given s and k, print n/k lines where each line i denotes string ui.

# Input Format

# The first line contains a single string denoting .
# The second line contains an integer, , denoting the length of each subsegment.

# Constraints

# , where  is the length of 
# It is guaranteed that  is a multiple of .
# Output Format

# Print  lines where each line  contains string .

# Sample Input

# AABCAAADA
# 3   
# Sample Output

# AB
# CA
# AD
# Explanation

# String  is split into  equal parts of length . We convert each  to  by removing any subsequent occurrences non-distinct characters in :

# We then print each  on a new line.


def merge_the_tools(string, k):
    # your code goes here
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            print (''.join(temp))
            temp = []
            len_temp = 0

if __name__ == '__main__':