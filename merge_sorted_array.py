class Solution(object):
    def merge_sorted_array(self,arr1,m,arr2,n):
        while m >0 and n> 0:
            if arr1[m-1] > arr2[n-1]:
                arr1[m+n-1] = arr1[m-1]
                m -= 1
            else:
                arr1[m+n-1] = arr2[n-1]
                n -= 1
        arr1[:n] == arr2[:n]
        return arr1



nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()
print(solution.merge_sorted_array(nums1,m,nums2,n))
