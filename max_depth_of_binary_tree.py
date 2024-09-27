class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Helper function to create a tree from a list representation
def create_tree_from_list(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    index = 1
    while index < len(lst):
        node = queue.pop(0)
        if lst[index] is not None:
            node.left = TreeNode(lst[index])
            queue.append(node.left)
        index += 1
        if index < len(lst) and lst[index] is not None:
            node.right = TreeNode(lst[index])
            queue.append(node.right)
        index += 1
    return root


# Example usage
if __name__ == "__main__":
    # Create trees from lists
    root1 = create_tree_from_list([3, 9, 20, None, None, 15, 7])
    root2 = create_tree_from_list([1, None, 2])

    # Create a Solution object
    solution = Solution()

    # Check the maximum depth of the trees
    print(solution.maxDepth(root1))  # Output: 3
    print(solution.maxDepth(root2))  # Output: 2