class Solution(object):
    def generate(self, numRows):
        result = []
        if numRows == 0:
            return result

        initial = [1]
        result.append(initial)

        for i in range(1, numRows):
            first_res = result[i-1]
            second = [1]

            for j in range(1,i):
                second.append(first_res[j-1] + first_res[j])

            second.append(1)
            result.append(second)
        return result
