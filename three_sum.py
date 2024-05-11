# Three sum from an array
def threeSum(nums):
    nums.sort()
    answer = []
    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        if nums[i] == nums[i-1]:
            continue
        while l < r:
            sums = nums[i] + nums[l] + nums[r]
            if sums > 0:
                r -= 1
            elif sums < 0:
                l +=1
            else:
                triplet = [nums[i], nums[l], nums[r]]
                triplet.append(answer)
                while l<r and nums[l] == triplet[1]:
                    l +=1
                while l<r and nums[r] == triplet[2]:
                    r-=1
        return answer



