def climbing_Staris(n):
    if n==1:
        return 1
    one = 1
    two = 1
    total =0
    for i in range(2,n+1):
        total = one + two
        two = one
        one = total
    return total


