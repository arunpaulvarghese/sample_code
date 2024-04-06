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




# class Solution(object):
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False
#         char_count = [0] * 26
#         for char in s:
#             char_count[ord(char) - ord('a')] += 1
#
#         for char in t:
#             if char_count[ord(char) - ord('a')] < 1:
#                 return False
#
#             char_count[ord(char) - ord('a')] -= 1
#         return True
#
#
# s = "anagram"
# t = "nagaram"
# result = Solution()
# print(result.isAnagram(s,t))


# class Solution(object):
#     def lengthOfLastWord(self, s):
#         length = 0
#         i = len(s) - 1
#         while i >= 0 and s[i] == ' ':
#             i -= 1
#         while i >= 0 and s[i] != ' ':
#             length += 1
#             i -= 1
#         return length
# s = "hello world "
# result = Solution()
# print(result.lengthOfLastWord(s))


# class Solution(object):
#     def plusOne(self, digits):
#         for i in range(len(digits)):
#             last = digits[i]
#         if last == 9:
#             digits[i] = 0
#         else:
#             digits[i] = last + 1
#             return digits
#         return [1] + digits
#
# s = [1,2,3]
# result = Solution()
# print(result.plusOne(s))



# Length of a substring without repeaitng the characters
# def lenthOfString(s):
#     seen = {}
#     length = 0
#     l = 0
#     for r in range(len(s)):
#         temp = s[r]
#         if temp in seen and seen[temp] >= l:
#             l = seen[temp] + 1
#         else:
#             length = max(length, r - l +1)
#         seen[temp] = r
#     return length
#
#
# stri = "abcacbdd"
# print(lenthOfString(stri))





# Insertion Sort

# def insertionSort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i-1
#         while j>= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key



# Longest common prefix
#
# def LongestPrefix(strs):
#     if len(strs) == 0:
#         return ""
#     base = strs[0]
#     for i in range(len(strs)):
#         for word in strs[1:]:
#             if (i == len(word) or word[i] != base[i]):
#                 return base[0:i]
#     return base
#
#
# arr = ["flower", "flow", "flo"]
# print(LongestPrefix(arr))






# -------------------------------------

# Two sums

# def TwoSums(target,nums):
#      sets = {}
#      for i in range(len(nums)):
#          second = target - nums[i]
#          if second in sets:
#              return sets[second], i
#          else:
#              sets[nums[i]] = i
#
# nums = [2,5,6,3]
# target = 9
# print(TwoSums(target,nums))







# Length of last word'

# def LengthOfLast(word):
#     length = 0
#     i = len(word)-1
#     while i>=0 and word[i] == '':
#         i -= 1
#     while i>=0 and word[i] != '':
#         length +=1
#         i -=1
#     return length


# Longest substring without repeating characters


# def LongestSubstring(string):
#     l = 0
#     lenght = 0
#     sets = {}
#     for r in range(len(string)):
#         char = string[r]
#         if char in sets and sets[char] >=l:
#             l = sets[char] + 1
#         else:
#             lenght = max(lenght, r-l + 1)
#         sets[char] = r
#     return lenght
#
# s = "abcfar"
# print(LongestSubstring(s))



# Insertion sort without swapping two variables


# def InsertionSort(stri):
#     for i in range(1,len(stri)):
#         j = i-1
#         key = stri[i]
#         while stri[j] > key and j>=0:
#             stri[j+1] = stri[j]
#             j -= 1
#         stri[j+1] = key
#     return stri
#
#
# s = [3,5,7,2,1,9]
# print(InsertionSort(s))







# Longest Common Prefix



# def LongestCommon(arr):
#     fir = arr[0]
#     for i in range(len(fir)):
#         for word in fir[1:]:
#             if word[i] != fir[i]:
#                 return word[0:i]
#     return word



# Roman to numerals

# def RomanToNumerals(s):
#     roman = {
#         'I' : 1,
#         'V' : 5,
#         'X' : 10,
#         'L' : 50,
#         'C' : 100,
#         'D' : 500,
#         'M' : 1000
#     }
#     total = 0
#     for i in range(len(s)-1):
#         if roman[s[i]] < roman[s[i+1]]:
#             total -= roman[s[i]]
#         else:
#             total += roman[s[i]]
#         total = total + roman[s[-1]]
#     return total
# n = "XVMLI"
# print(RomanToNumerals(n))









# Valid Paranthesis


# def isValid(s):
#     dictt = {
#         '(' : ')',
#         '{' : '}',
#         '[' : ']'
#     }
#     stack = []
#     for para in s:
#         if para in dictt:
#             stack.append(para)
#         elif len(stack) == 0 or para != dictt[stack.pop()]:
#             return False
#     if len(stack) == 0:
#         return True
#     else:
#         return False
#
# d = "{([])}"
# isValid(d)




# Palindrome

# def Palindrome(x):
#         set1 = []
#         set2 = []
#         for i in range(len(x)):
#             j = len(x) - 1
#             set1.append(x[i])
#             set2.append(x[j-i])
#
#
#         if set1 != set2:
#             print("Not Palindrome")
#         else:
#             print("Palindrome")
#
#
# s = "Malayalam"
# print(Palindrome(s))









# Longest palindrome substring

#
# def LongestPalindrome(s):
#     def Expand(r,l):
#         while(l >=0 and r > len(s) and s[r] == s[l]):
#             l -= 1
#             r += 1
#         return s[l+1: r]
#
#     result = ""
#     for i in range(len(s)):
#         res1 = Expand(i,i)
#         if len(res1) >len(result):
#             result = res1
#         res2 = Expand(i, i+1)
#         if len(res2) > len(result):
#             result = res2
#     return result
#
# n = "abaab"
# print(LongestPalindrome(n))



# Predict the stock price

# def StockPrice(s):
#     total = 0
#     buy = s[0]
#     for sell in s[1:]:
#         if sell > buy:
#             total = max(total, sell - buy)
#         else:
#             buy = sell
#     return total





# Stone Paper cissors game
#
# import random
#
# def user_wins(user, computer):
#     if (user == 'rock' and computer == 'scissors' or
#         user == 'paper' and computer == 'rock' or
#         user == 'scissors' and computer == 'paper'):
#         return True
#     return False
#
# def user_input():
#     user = input("Enter stone,paper,scissor")
#     user = user.lower().strip()
#     return user
#
# def main():
#     user_score = 0
#     computer_score = 0
#     user =""
#     print("Enter END to terminate")
#     while user != "end":
#         print(f"score{computer_score} - {user_score}")
#         computer = random.choice(["stone","paper","scissors"])
#         user = user_input()
#         if user == 'end':
#             print('Session Terminated')
#         elif user == computer:
#             print(f"select {computer} so its a tie")
#         elif user_wins(user,computer):
#             print(f"you select {computer} you wins")
#             user_score += 1
#         else:
#             print(f"i choose {computer}, you win")
#             computer_score += 1
#
#
# if __name__ == "__main__":
#     main()






#Contains Duplicats
# def DuplicateElements(s):
#     d = []
#     for i in range(len(s)):
#         if s[i] in d:
#
#         else:
#             d.append(s[i])
# s = [4,5,3,5]
# print(DuplicateElements(s))







# def removeDuplicates(nums):
#     dupli = []
#     for i in range(len(nums)):
#         if nums[i] in dupli:
#             pass
#         else:
#             dupli.append(nums[i])
#     return dupli
#
# s = [1,5,4,6,6]
# print(removeDuplicates(s))





# Container with most water
# def containerWater(vals):
#     max_area = 0
#     l = 0
#     r = len(vals) - 1
#     while l < r:
#         area = (r-l) * min(vals[l], vals[r])
#         max_area = max(area, max_area)
#         if vals[l] > vals[r]:
#             r -= 1
#         else:
#             l +=1
#     return max_area
#
# s = [4,6,7,3,5,2]
# print(containerWater(s))






# Watter trapping

# def wateTrapping(nums):
#     ans = 0
#     i = 1
#     j = len(nums) - 1
#     lmax = nums[0]
#     rmax = nums[-1]
#     while i <= j:
#         if nums[i] > lmax:
#             lmax = nums[i]
#         if nums[j] > rmax:
#             rmax = nums[j]
#
#         if lmax < rmax:
#             ans += lmax - nums[i]
#             i +=1
#         else:
#             ans += lmax - nums[j]
#             j -=1
#     return ans




#remove duplicates from a sorted array

# def duplicates(nums):
#     dupli = []
#     for i in range(len(nums)):
#         if nums[i] == nums[i-1]:
#             pass
#         else:
#             dupli.append(nums[i])
#     return dupli
#
# n = [5,5,6,7,7,8]
# print(duplicates(n))



#remove duplicates form a sorted array

# def removeDuplicates(nums):
#     replace = 1
#     for i in range(1,len(nums)):
#         if nums[i-1] != nums[i]:
#             nums[replace] = nums[i]
#             replace +=1
#     return replace
#
# n = [5,5,6,7,7,8]
# print(removeDuplicates(n))



#remove an element

# def removeElement(nums, element):
#     i = 0
#     for n in nums:
#         if n != element:
#             nums[i] = n
#             i +=1
#     return n
#
# ele = 6
# n = [5,5,6,7,7,8]
# print(removeElement(n, ele))




# Longest substring without repeating characters

# def longestSubstring(nums):
#     length = 0
#     l = 0
#     sample ={}
#     for r in range(len(nums)):
#         temp = nums[r]
#         if temp in sample and sample[temp] >= l:
#             l = sample[temp] + 1
#         else:
#             length = max(length, r-l + 1)
#         sample[temp] = r
#     return length



#Search Insert position using binary search and O(logn)

# def insertSearch(num, target):
#     l = 0
#     r = len(num) - 1
#     while l <= r:
#         mid = (r+l) // 2
#         if num[mid] < target:
#             l = mid + 1
#         elif num[mid] > target:
#             r = mid - 1
#         else:
#             return mid
#     return l


# def zigZag(nums, numRows):
#     if numRows == 0 and numRows <= len(nums):
#         return False
#     index = 0
#     step = 1
#     Rows = [[] for row in range(numRows)]
#     for i in nums:
#         Rows[index].append(i)
#         if index == 0:
#             step = 1
#         elif index == numRows - 1:
#             step = -1
#         index = index+ step
#
#     for i in range(numRows):
#         Rows[i] = ''.join(Rows[i])
#     return ''.join(Rows)
#
#
# n = 'helloworld'
# print(zigZag(n,3))



# Find Index of first occurance

# def indexOfFirst(needle):
#     val = 0
#     elf = [0] * len(needle)
#     for i in range(1,len(needle)):
#         while val > 0 and needle[i] != needle[val]:
#             val = elf[val-1]
#         if needle[i] == needle[val]:
#             val +=1
#             elf[i] = val
#     return elf
#
# n = 'a,b,s,a,f,a'
# print(indexOfFirst(n))







# Find the first occurance of a string

# def string_First(needle,haystack):
#     lpf = [0] * len(needle)
#     pre = 0
#     n = 0
#     for i in range(1,len(needle)):
#         while pre > 0 and needle[i] != needle[pre]:
#             pre = lpf[pre - 1]
#         if needle[i] == needle[pre]:
#             pre += 1
#             lpf[i] = pre
#
#     for j in range(len(haystack)):
#         while n > 0 and haystack[j] != needle[n]:
#             n = lpf[n-1]
#         if haystack[j] == needle[n]:
#             n += 1
#
#         if n == len(needle):
#             return j-n+1
#
#     return -1


# 3 sum of a number in an array should be zero

def threeSum(nums):
    nums.sort()
    answer = []
    for i in range(len(nums)-2):
        if i >0 and nums[i] == nums[i+1]:
            continue
        l = i + 1
        r = len(nums)- 1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l +=1
            else:
                triplet = [nums[i], nums[l], nums[r]]
                answer.append(triplet)
                while l < r and nums[l] == triplet[1]:
                    l+=1
                while l < r and nums[r] == triplet[2]:
                    r -= 1
        return answer














































