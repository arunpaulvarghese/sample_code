class Solution(object):
    def square_root(self,nums):
        if nums == 0:
            return 0
        for i in range(1,nums):
            if i * i == nums:
                return i
            elif i*i > nums:
                return i-1
        return i

solution = Solution()
print(solution.square_root(20))


