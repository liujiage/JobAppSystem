from array import *
from random import randrange
from time import time

from llist import sllist, sllistnode


class ListVSLinkedListTest:
    pass


simpleList = list()
for v in range(1000000):
    simpleList.append(v)
start = time()
for v in range(1000):
    simpleList.insert(randrange(1000000), v)
end = time()
print("list spend time %f, total size: %d" % (end - start, len(simpleList)))

# init linkedList
linkedList = sllist()
for v in range(1000000):
    linkedList.append(v)
# random insert into list
start = time()
for v in range(1000):
    linkedList.insertafter(v, linkedList.nodeat(randrange(1000000)))
end = time()
print("linkedList spend time %f, total size: %d" % (end - start, len(linkedList)))

'''linkedList = sllist([1, 2, 3])
print(len(linkedList), linkedList.size)
print(linkedList.nodeat(0), linkedList[0])
firstNode = linkedList.first
print("first node is %s , value is %d" % (firstNode, firstNode.value))
for value in linkedList:
    print(value)
linkedList.appendright(4)
print(linkedList)
linkedList.append(5)
print(linkedList)
linkedList.appendnode(sllistnode(6))
print(linkedList)'''
