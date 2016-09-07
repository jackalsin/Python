class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def toString(self):
        return "val = " + self.val + "\tleft = " + self.left + "\tright = " + self.right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    prev = None
    def isValidBST(self, root):
        def valid(node):
            if not node: return True
            if not valid(node.left): return False
            if self.prev and self.prev.val>=node.val: return False
            self.prev = node
            return valid(node.right)
        return valid(root)

def main():
    solution = Solution()
    # node1 = TreeNode(1)
    # node2 = TreeNode(2)
    # node3 = TreeNode(3)
    # node4 = TreeNode(4)
    # node5 = TreeNode(5)
    # node6 = TreeNode(6)
    # node7 = TreeNode(7)
    # node4.left = node2
    # node4.right = node6
    # node2.left = node1
    # node2.right = node3
    # node6.left = node5
    # node6.right = node7

    # print solution.isValidBST(node4)

    newNode1 = TreeNode(1)
    newNode1.left = TreeNode(1)

    print solution.isValidBST(newNode1)
main()