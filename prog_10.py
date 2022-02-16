'''
To read the last element from each row and sum of the all last elements. For example:
Input
[[8, 14, -6], [12,7,4], [-11,3,21]]
Output
19
'''

ls = [[8, 14, -6], [12,7,4], [-11,3,21]]
#print(sum(x[-1] for x in ls))

summ = 0 
for x in ls :
    summ = summ + x[-1]
print(summ)