class Solution(object):
    def removeDuplicates(self, nums):
        pass





nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution()
k = solution.removeDuplicates(nums)
print(f"Number of unique elements: {k}")
print(f"Modified nums: {nums[:k]}")