'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''
class Node:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.nextNode = nextNode

def findIntersectingNode(linkList1, linkList2):
    node1 = linkList1
    node2 = linkList2

    while node1.val != node2.val:
        node1 = node1.nextNode if node1.nextNode != None else linkList2
        node2 = node2.nextNode if node2.nextNode != None else linkList1

    return node1.val

linklist1 = Node(1, Node(2, Node(3, Node(4))))
linklist2 = Node(9, Node(8, Node(7, Node(3, Node(4)))))

print findIntersectingNode(linklist1, linklist2)
