class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n & 1  # Add 1 if the last bit is set
            n >>= 1         # Shift n to the right to check the next bit
        return count

# Create an instance of the Solution class
sol = Solution()

# Test cases
input1 = 11    # Binary: 1011, expected output: 3
output1 = sol.hammingWeight(input1)
print(f"Input: {input1}, Output: {output1}")

input2 = 128   # Binary: 10000000, expected output: 1
output2 = sol.hammingWeight(input2)
print(f"Input: {input2}, Output: {output2}")

input3 = 2147483645  # Binary: 1111111111111111111111111111101, expected output: 30
output3 = sol.hammingWeight(input3)
print(f"Input: {input3}, Output: {output3}")
