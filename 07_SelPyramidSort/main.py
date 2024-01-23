def SelSort(a):
    for i in range(len(a)):
        t = a[i]
        mI = getMin(a[i:]) + i
        a[i] = a[mI]
        a[mI] = t
    return a

def getMin(a):
    m = 0
    for i in range(1, len(a)):
        if a[i] < a[m]:
            m = i
    return m

def HeapSort(a):
    for i in range(len(a), -1, -1):
        Heapify(a, i, len(a))
    for i in range(len(a)-1, -1, -1):
        t = a[0]
        a[0] = a[i]
        a[i] = t
        Heapify(a, 0, i)
    return a

def Heapify(a, root, size):
    x = root
    l = x * 2 + 1
    r = l + 1
    if size > l and a[l] > a[x]:
        x = l
    if size > r and a[r] > a[x]:
        x = r
    if x == root:
        return
    t = a[root]
    a[root] = a[x]
    a[x] = t
    Heapify(a, x, size)

a = [2, 1, 5, 4, 6, 9, 7]

print(HeapSort(a))