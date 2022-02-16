#from collections import deque

'''
queue = []
#queue add the item

queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

#delete item
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print(queue)

queue.pop(0)

'''
'''
q = deque()

#add item
q.append('a')
q.append('b')
q.append('c')

print(q)

#remove item

print(q.popleft())
print(q.popleft())
print(q.popleft())

print(q)
'''
# Python program to
# demonstrate implementation of
# queue using queue module


from queue import Queue

# Initializing a queue
q = Queue(maxsize = 3)

# qsize() give the maxsize
# of the Queue
print(q.qsize())

# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')

# Return Boolean for Full
# Queue
print("\nFull: ", q.full())

# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty
# Queue
print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())

# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())

