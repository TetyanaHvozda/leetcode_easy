class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        text = ''.join([char for char in s if char.isalnum()]).lower()
        reverse = text[::-1]
        print(text)
        print(reverse)

        return text == reverse

s = "A man, a plan, a canal: Panama"

# Creating a solution instance
solution = Solution()

output = solution.isPalindrome(s)

# Output the result
print(output)
