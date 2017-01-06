class binaryTreeNode: # Represents nodes in binary tree

    # Task 1.a. This __init__ method is not completed. Please add the missing code.
    # This is the constructor to create a node.
    # @param value represents the node value.
    def __init__(self, value):
        self.leftchild = None
        self.rightchild = None # When you create a Node, it doesn't have children, so set them to None
        self.value = value


    def insertNode(self, newValue):
        # Task 1.b. This insertNode method only contains the code to insert a node if the value is smaller
        # than the value of current node. Please complete this code for the value that is larger than
        # the current node.

        # The rules of INSERT operation are as follows:
        # 1. If the value of new node is less than or equal to the value of current node,
        #    AND the left child of current node is not None (so you can't insert as left child since it is occupied),
        #    then use the LEFT child as new parent node and call "insertNode" function again.
        # 2. If the value of new node is larger than the value of current node,
        #    AND the right child of current node is not None (so you can't insert as right child since it is occupied),
        #    then use the Right child as new parent node and call "insertNode" function again.
        if newValue <= self.value:
            if self.leftchild is not None:
                self.leftchild.insertNode(newValue)
            else:
                self.leftchild = binaryTreeNode(newValue)
        else:
            if self.rightchild is not None:
                self.rightchild.insertNode(newValue)
            else:
                self.rightchild = binaryTreeNode(newValue)

    def outputPreOrder(self):
        # This method will print the tree in Pre-order
        print self.value
        if self.leftchild is not None:
            self.leftchild.outputPreOrder()
        if self.rightchild is not None:
            self.rightchild.outputPreOrder()

    # Task 1.c. Please write a new method outputInOrder, to print out data in order.
    def outputInOrder(self):
        if (self.leftchild is not None):
            self.leftchild.outputInOrder()
        print self.value
        if self.rightchild is not None:
            self.rightchild.outputPreOrder()


class myBST: # Represents binary search tree structure
    def __init__(self, root): # Initialize a binary search tree with a root, which is a "binaryTreeNode"
        self.root = root

    def insert(self, newNode): # Insert a new node into this binary search tree, call "insertNode" function below
        self.root.insertNode(newNode)


    def outputPreOrder(self): # Call "outputPreOrder" function below
        self.root.outputPreOrder()

    def outputInOrder(self):
        self.root.outputInOrder()


tree = myBST(binaryTreeNode(10)) # Create a BST instance called "tree". The value of root node is 10.
for number in [20, 48, 51, 9, 22, 2015, 3, 3, 2, 2, 1]:
    # Task 1.d. Use intergers in this list as the values of new nodes and insert them into "tree" here (JUST ONE LINE!)
    tree.insert(number)

# Output the values stored in your "tree" in non-decreasing order here (JUST ONE LINE!)
print "Print out the numbers in Pre-order travel:"
tree.outputPreOrder()
print "Print out the numbers in In-order travel:"
tree.outputInOrder()