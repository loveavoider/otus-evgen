def Split(a, L, R): 
    m = L - 1 
    p = a[R] 
    for j in range(L, R+1): 
        if a[j] <= p: 
            m += 1 
            t = a[j] 
            a[j] = a[m] 
            a[m] = t 
    return m 
 
def QSort(a, L, R): 
    if L >= R: 
        return 
    q = Split(a, L, R) 
    QSort(a, L, q-1) 
    QSort(a, q, R) 
    return a
 
def Merge(a, L, M, R): 
    i, j = L, M+1 
    arr = [] 
    while i <= M and j <= R: 
        if a[i] > a[j]: 
            arr.append(a[j]) 
            j += 1 
        else: 
            arr.append(a[i]) 
            i += 1 
    while (i <= M): 
        arr.append(a[i]) 
        i += 1 
    while (j <= R): 
        arr.append(a[j]) 
        j += 1 
    a[L:R+1] = arr 
    return arr 
 
 
def MSort(a, L, R): 
    if L >= R: 
        return 
    M = (L + R) // 2 
    MSort(a, L, M) 
    MSort(a, M + 1, R) 
    Merge(a, L, M, R) 
    return a 
 
a = [4, 1, 2, 5, 7, 9, 3]