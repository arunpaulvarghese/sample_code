# Product of anarray except self
def productOfArrayExceptSelf(nums):
    length = len(nums)
    product = [1] * length
    for i in range(1,length):
        product[i] = nums[i-1] * product[i-1]
    sample = nums[-1]
    for i in range(length-2, -1, -1):
        product[i] = product[i] * sample
        sample = nums[i] * sample
    return product

