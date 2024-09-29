class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def recursive(node):
            if not node:
                return 0

            count_left = recursive(node.left)
            if count_left == -1:
                return -1

            count_right = recursive(node.right)
            if count_right == -1:
                return -1

            if abs(count_left - count_right) > 1:
                return -1

            return 1 + max(count_left, count_right)

        return recursive(root) != -1


# Helper function to build the binary tree from a list
def build_tree_from_list(lst):
    if not lst:
        return None

    from collections import deque
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):
        current = queue.popleft()

        if i < len(lst) and lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1

        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1

    return root


# Example 1
root_list = [3, 9, 20, None, None, 15, 7]
root = build_tree_from_list(root_list)
solution = Solution()
print(solution.isBalanced(root))  # Output: True

# Example 2
root_list = [1, 2, 2, 3, 3, None, None, 4, 4]
root = build_tree_from_list(root_list)
print(solution.isBalanced(root))  # Output: False

# Example 3
root_list = []
root = build_tree_from_list(root_list)
print(solution.isBalanced(root))  # Output: True

