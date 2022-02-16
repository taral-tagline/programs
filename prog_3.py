'''
Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length. For example:
Input:
[
[1, 2, 3, 4,5],
[5, 6, 7, 8,6],
[9, 10, 11, 12,7],
]
Output:
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
'''

ls = [[1,2,3,4,5,0,11],[5,6,7,8,6,0,11],[9,10,11,12,7,0,11]]

new_list = []
for j in range(len(ls)) :
    for i in range(len(ls[0])) :
        inner_item = []
    for item in ls :
        inner_item.append(item[i])
    new_list.append(inner_item)
print(new_list)

#print(ls)
#ls1 = [[row[i] for row in ls] for i in range(4)]
#print(ls1)
'''
new_list = []
for i in range(len(ls[0])) :
    inner_item = []
    for item in ls :
        inner_item.append(item[i])
    new_list.append(inner_item)
print(new_list)
'''