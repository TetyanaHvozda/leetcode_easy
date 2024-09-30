class Solution(object):
    def generate(self, rowIndex):
        triangle = []
        for i in range(rowIndex + 1):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)
        return triangle[rowIndex]

rowIndex = 3

# Creating a solution instance
solution = Solution()

output = solution.generate(rowIndex)

# Output the result
print(output)