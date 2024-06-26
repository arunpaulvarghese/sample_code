class Solution(object):
    def getRow(self, rowIndex):
        result = []
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        rowIndex = rowIndex + 1
        start_row = [1]
        result.append(start_row)
        for i in range(1,rowIndex):
            prev_row = result[i-1]
            curr_row = [1]

            for j in range(1, i):
                curr_row.append(prev_row[j-1] + prev_row[j])

            curr_row.append(1)
            result.append(curr_row)

        return result[-1]


result = Solution()
print(result.getRow(4))
