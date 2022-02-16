'''
Flatten a list using list comprehension and for loop.
For example:
Input:
[[1,2,3], [4,5,6], [7,8,9]]
Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

ls = [[1,2,3], [4,5,6], [7,8,9]]
#one_ls =[]
one_ls = [ item for elem in ls for item in elem]
#for elem in ls :
#    for item in elem :
#        one_ls.append(item)
print(one_ls)