#remove duplicates form a sorted array

def removeDuplicates(nums):
    replace = 1
    for i in range(1,len(nums)):
        if nums[i-1] != nums[i]:
            nums[replace] = nums[i]
            replace +=1
    return replace

n = [5,5,6,7,7,8]
print(removeDuplicates(n))
