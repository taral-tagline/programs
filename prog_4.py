'''
Find the even elements from an array. Respectively multiply this element in the array.
For example:
Input:
[1, 2, 3, 4, 5]
Output
[4,8]
(Note: Need one line code, don't use for loop and if statement).
'''
#import math

ls = [1, 2, 3, 5, 4]
print(list(map(lambda x : x*2 , filter(lambda x : (x%2 == 0),ls))))
