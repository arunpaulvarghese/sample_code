def isValid(s):
    dictt = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
    stack = []
    for para in s:
        if para in dictt:
            stack.append(para)
        elif len(stack) == 0 or para != dictt[stack.pop()]:
            return False
    if len(stack) == 0:
        return True
    else:
        return False

d = "{([])}"
isValid(d)


# sample code
