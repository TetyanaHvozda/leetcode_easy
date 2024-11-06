# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Base case: if the root is None, just return None
        if root is None:
            return None

        # Recursively invert the left and right subtrees
        root.left, root.right = root.right, root.left

        # Invert the left subtree
        self.invertTree(root.left)

        # Invert the right subtree
        self.invertTree(root.right)

        return root


# Helper function to print the tree in level order (for testing purposes)
from collections import deque


def print_tree(root):
    if not root:
        print("Tree is empty")
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            print(node.val, end=' ')
            queue.append(node.left)
            queue.append(node.right)
        else:
            print("None", end=' ')
    print()


# Example usage
if __name__ == "__main__":
    # Create a binary tree: [4, 2, 7, 1, 3, 6, 9]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("Original tree:")
    print_tree(root)

    # Invert the tree
    solution = Solution()
    inverted_root = solution.invertTree(root)

    print("Inverted tree:")
    print_tree(inverted_root)
