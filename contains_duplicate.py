class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


solution = Solution()

nums = [1,2,3,1]

print(solution.containsDuplicate(nums))