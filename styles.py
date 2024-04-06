# Find Index of first occurance

def indexOfFirst(needle):
    val = 0
    elf = [0] * len(needle)
    for i in range(1,len(needle)):
        while val > 0 and needle[i] != needle[val]:
            val = elf[val-1]
        if needle[i] == needle[val]:
            val +=1
            elf[i] = val
    return elf

n = 'a,b,s,a,f,a'
print(indexOfFirst(n))


#Search Insert position using binary search and O(logn)

def insertSearch(num, target):
    l = 0
    r = len(num) - 1
    while l <= r:
        mid = (r+l) // 2
        if num[mid] < target:
            l = mid + 1
        elif num[mid] > target:
            r = mid - 1
        else:
            return mid
    return l
