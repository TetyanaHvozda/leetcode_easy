from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]


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
output = solution.postorderTraversal(root)

# Output the result
print(output) #[4,6,7,5,2,9,8,3,1]