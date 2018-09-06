'''

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

     0
    / \
   1   0
      / \
     1   0
    / \
   1   1
'''
class Node:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

def findUniversalValue(tree):
    if tree == None:
        return 0, True
    leftCnt, isLeftUniversal = findUniversalValue(tree.left)
    rightCnt, isRightUniversal = findUniversalValue(tree.right)
    # all sub tree is complete, compute total count
    totalCnt = leftCnt + rightCnt
    # if left and right subtrees are universal, check self is universal tree or not
    if isLeftUniversal and isRightUniversal:
        if tree.left is not None and tree.root != tree.left.root:
            return totalCnt, False
        if tree.right is not None and tree.root != tree.right.root:
            return totalCnt, False
        # self is universal tree, count + 1
        return totalCnt + 1, True

    return totalCnt, False

tree1 = Node(1)
tree2 = Node(1)
tree3 = Node(1, tree1, tree2)
tree4 = Node(0)
tree5 = Node(0, tree3, tree4)
tree6 = Node(1)
tree7 = Node(0, tree6, tree5)

cnt, _ = findUniversalValue(tree7)
print cnt
