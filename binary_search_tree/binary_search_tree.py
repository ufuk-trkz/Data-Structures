"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
            # if there is no left child
                # insert value here
            # ELSE ???
                # repeat the process on left subtree 
        # Case 2: value is greater than or equal self.value      
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value is target:
            return True
        # Case 2: target is less than self.value
        elif target < self.value:
            #if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        # iterate through the nodes using a loop construct
        while self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursive solution
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        if self is None:
            return
        # (base case) we want to return
        # check if we can move left
        if self.left:
            self.left.in_order_print()
        # visit the note by printing it's value
        print(self.value)
        # check if we can move right
        if self.right:
            self.right.in_order_print()

        # if node:
        #     self.in_order_print(node.left)
        #     print(node.value)
        #     self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
    # Use a queue to from a "line"
    # for the nodes to "get in"
        queue = Queue()
        queue.enqueue(node)

        while queue.size != 0:
            selectedNode = queue.dequeue()
            print(selectedNode.value)
            if selectedNode.left:
                queue.enqueue(selectedNode.left)
            if selectedNode.right:
                queue.enqueue(selectedNode.right)

    # start by placing the root in the queue
    # need a while loop to iterate
    # what are we checking in the while statement?
    # while length of queue is greater than 0
        # dequeue item from front of queue
        # print that item

        # place current item's left node in queue if not None
        # place current item's right node in queue if not None

    # place left node in queue if not None

    # place right node in queue if not None

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
    # initialize an empty stack
    # push the root node onto the stack
        stack = Stack()
        stack.push(node)

        while stack.size != 0:
            selectedNode = stack.pop()
            print(selectedNode.value)
            if selectedNode.left:
                stack.push(selectedNode.left)
            if selectedNode.right:
                stack.push(selectedNode.right)

    # need a while loop to manage our iteration
    # if stack is not empty enter the while loop
        # pop item off the stack
        # print that item's value

        # if there is a left subtree
            # push left item onto the stack
        
        # if there is a right subtree
            # push right item onto the stack


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
