# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # If both nodes are None, trees are the same
        if not p and not q:
            return True

        # If one of the nodes is None, trees are not the same
        if not p or not q:
            return False

        # If the values of the current nodes are different, trees are not the same
        if p.val != q.val:
            return False

        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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
    p = create_tree_from_list([1, 2])
    q = create_tree_from_list([1, None, 2])

    # Create a Solution object
    solution = Solution()

    # Check if the two trees are the same
    result = solution.isSameTree(p, q)
    print(result)  # Output: False
