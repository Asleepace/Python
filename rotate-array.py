def rotateImage(a):
    n = len(a)
    s = n / 2
    for i in range(0,n):
        for j in range(i,n):
            a[i][j],a[j][i] = a[j][i],a[i][j]
        for j in range(0,s):
            a[i][j],a[i][n-j-1] = a[i][n-j-1],a[i][j]
    return a