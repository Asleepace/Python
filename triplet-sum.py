def tripletSum(x, a):
    pairs = {}
    size = len(a)
    for i in range(0,size):
        for j in range(i+1,size):
            pairs[a[i]+a[j]] = [i,j]
    
    for i in range(0,size):
        key = x-a[i]
        if key in pairs:
            if pairs[key][0] != i and pairs[key][1] != i:
                return True
    
    return False
