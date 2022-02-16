'''
Write a program.
For example:
Input
[56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
Output
[56.2, 51.7, 55.3, 52.5, 47.8]
'''

data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
for item in data :
    if item != item:
        data.remove(item)
print(data)