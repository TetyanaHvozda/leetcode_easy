from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


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
root_list = [1, 2]
targetSum = 1

# Building the tree from the list
root = build_tree_from_list(root_list)

# Creating a solution instance
solution = Solution()

# Getting the inorder traversal of the tree
output = solution.hasPathSum(root, targetSum)

# Output the result
print(output)