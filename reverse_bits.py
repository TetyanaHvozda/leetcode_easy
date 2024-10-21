class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            # Shift result to the left to make space for the next bit
            result <<= 1
            # Add the least significant bit of n to the result
            result |= (n & 1)
            # Shift n to the right to process the next bit
            n >>= 1
        return result


# Create an instance of the Solution class
sol = Solution()

# Example 1: Input as a decimal number (binary representation 00000010100101000001111010011100)
input1 = 43261596
output1 = sol.reverseBits(input1)
print(f"Input: {input1} -> Reversed Output: {output1}")

# Example 2: Input as a decimal number (binary representation 11111111111111111111111111111101)
input2 = 4294967293
output2 = sol.reverseBits(input2)
print(f"Input: {input2} -> Reversed Output: {output2}")