class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = [num for num in nums if nums.count(num) == 1]
        result = int(single[0])
        return result

nums = [4,1,2,1,2]

# Creating a solution instance
solution = Solution()

output = solution.singleNumber(nums)

# Output the result
print(output)
