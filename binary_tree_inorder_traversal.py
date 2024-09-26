# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result



    # Creating a sample binary tree
    # Input: root = [1, null, 2, 3]
    # The tree looks like this:
    #   1
    #    \
    #     2
    #    /
    #   3

# Helper function to build the binary tree from a list
def build_tree_from_list(lst):
    if not lst:
        return None

    # Create the root of the tree
    root = TreeNode(lst[0])
    queue = deque([root])

    i = 1
    while queue and i < len(lst):
        current = queue.popleft()

        # Assign the left child
        if i < len(lst) and lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1

        # Assign the right child
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1

    return root

# Input list representing the tree structure
root_list = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]

# Building the tree from the list
root = build_tree_from_list(root_list)

# Creating a solution instance
solution = Solution()

# Getting the inorder traversal of the tree
output = solution.inorderTraversal(root)

# Output the result
print(output)  # Expected Output: [4, 2, 6, 5, 7, 1, 3, 9, 8]