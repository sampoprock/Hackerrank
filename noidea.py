# There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

# Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

# Constraints



# Input Format

# The first line contains integers  and  separated by a space.
# The second line contains  integers, the elements of the array.
# The third and fourth lines contain  integers,  and , respectively.

# Output Format

# Output a single integer, your total happiness.

# Sample Input

# 3 2
# 1 5 3
# 3 1
# 5 7
# Sample Output

# 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
i, j = input().split()

sc_ar = input().split()

m = set(input().split())
n = set(input().split())
print (sum([(i in m) - (i in n) for i in sc_ar]))
