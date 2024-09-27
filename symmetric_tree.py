class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(selfself, root):

        def recursive(leftroot, rightroot):
            if not leftroot and not rightroot:
                return True

            if not leftroot or not rightroot:
                return False

            if leftroot.val != rightroot.val:
                return False

            return recursive(leftroot.left, rightroot.right) and recursive(leftroot.right, rightroot.left)

        return recursive(root.left, root.right)


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
    root1 = create_tree_from_list([1, 2, 2, 3, 4, 4, 3])
    root2 = create_tree_from_list([1, 2, 2, None, 3, None, 3])

    # Create a Solution object
    solution = Solution()

    # Check if the trees are symmetric
    print(solution.isSymmetric(root1))  # Output: True
    print(solution.isSymmetric(root2))  # Output: False