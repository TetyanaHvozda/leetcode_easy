class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(selfself, nums):
        def recursive(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = recursive(left, mid - 1)
            root.right = recursive(mid +1, right)

            return root

        return recursive(0, len(nums) - 1)


# Helper function to print the tree in level order
def print_level_order(root):
    if not root:
        return "[]"

    from collections import deque
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()

    return result



# Example usage
if __name__ == "__main__":
    # Create a Solution object
    solution = Solution()

    # Example inputs
    nums1 = [-10, -3, 0, 5, 9]
    nums2 = [1, 3]

    # Convert arrays to BST
    bst1 = solution.sortedArrayToBST(nums1)
    bst2 = solution.sortedArrayToBST(nums2)

    print(print_level_order(bst1))  # Output: [0, -3, 5, -10, None, 9]
    print(print_level_order(bst2))  # Output: [3, 1]