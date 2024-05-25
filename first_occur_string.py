# Finding the index of the first occurance in a string

def indexString(needle, haystack):
    # Setting the lps values with the len of needle
    lps = [0] * len(needle)

    # assigning the lps values into the lps string
    pre = 0
    for i in range(1,len(needle)):
        while (pre >0 and needle[i] != needle[pre]):
            pre = lps[pre-1]
        if needle[i] == needle[pre]:
            pre +=1
            lps[i] = pre

    # comparing the needle and the haystack with the lps value
    n = 0
    for h in range(len(haystack)):
        while n >0 and needle[n] != haystack[h]:
            n = lps[n-1]
        if needle[n] == haystack[h]:
            n +=1
        if n == len(needle):
            return h-n+1
    return -1
