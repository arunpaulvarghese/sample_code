# class Solution(object):
#     def maxProductDifference(self, nums):
#         min_number = sec_min = float("inf")
#         max_number = sec_max = 0
#         for i in nums:
#             if i < min_number:
#                 sec_min = min_number
#                 min_number = i
#             elif i < sec_min:
#                 sec_min = i
#
#             if i > max_number:
#                 sec_max = max_number
#                 max_number = i
#             elif i > sec_max:
#                 sec_max = i
#
#         return (max_number * sec_max) - (min_number * sec_min)

