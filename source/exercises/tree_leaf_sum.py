
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def isLeaf(self):
        return self.left==None and self.right==None

    def internalLeftLeafSum(self, node, sense):

        if node == None:
            return 0

        if node.isLeaf() and "L" == sense:
            return node.val

        return self.internalLeftLeafSum( node.left, "L")+ self.internalLeftLeafSum( node.right, "R")
    def getLeftLeafSum(self):
        return self.internalLeftLeafSum( self.left, "L")+ self.internalLeftLeafSum( self.right, "R")
        
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

    n3= TreeNode(15)
    n4= TreeNode(7)
    n1= TreeNode(9)
    n2= TreeNode(20, n3, n4)
    root= TreeNode(3, n1, n2)

    print(root.getLeftLeafSum())

    n5= TreeNode(6)
    n4= TreeNode(3)
    n3= TreeNode(2)
    n2= TreeNode(7, n4, n5)
    n1= TreeNode(3, n3)
    root= TreeNode(1, n1, n2)

    print(root.getLeftLeafSum())
