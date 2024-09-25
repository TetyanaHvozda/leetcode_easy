# Definition for a binary tree node.
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

if __name__ =="__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    # Create a solution instance
    solution = Solution()

    # Get the inorder traversal
    output = solution.inorderTraversal(root)
    print(output)  # Output: [1, 3, 2]