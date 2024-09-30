class Solution(object):
    def generate(self, numRows):
        triangle = []
        for i in range(numRows):
            row = [1] * (i+1)
            print(row)

            for j in range(1, i):
                row[j] = triangle[i-1][j-1]+triangle[i-1][j]
                val = row[j]
                print(j, val)

            triangle.append(row)

        return triangle

numRows = 5

# Creating a solution instance
solution = Solution()

output = solution.generate(numRows)

# Output the result
print(output)