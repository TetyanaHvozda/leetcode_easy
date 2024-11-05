# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Helper function to calculate the depth of the leftmost path.
        def left_depth(node):
            depth = 0
            while node:
                node = node.left
                depth += 1
            return depth

        # Helper function to calculate the depth of the rightmost path.
        def right_depth(node):
            depth = 0
            while node:
                node = node.right
                depth += 1
            return depth

        if not root:
            print("Tree is empty")
            return 0

        # Calculate left and right depths
        left = left_depth(root)
        right = right_depth(root)

        print(f"Current root value: {root.val}")
        print(f"Left depth: {left}")
        print(f"Right depth: {right}")

        # If left and right depths are the same, it's a perfect binary tree
        if left == right:
            total_nodes = (2 ** left) - 1
            print(f"Perfect binary tree detected with depth {left}. Total nodes: {total_nodes}")
            return total_nodes

        # Otherwise, recursively count nodes in left and right subtrees
        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)
        total_nodes = 1 + left_count + right_count

        print(f"Subtree with root {root.val} has total nodes: {total_nodes}")
        return total_nodes


# Example usage:
# Creating the tree for root = [1, 2, 3, 4, 5, 6]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

solution = Solution()
print("Total nodes in the tree:", solution.countNodes(root))
