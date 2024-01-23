def insertSort(arr):
    for i in range(1, len(arr)):
        t = arr[i]
        count = 0
        for j in range(i, 0, -1):
            if t > arr[j]:
                break
            arr[j] = arr[j-1]
            count += 1
        arr[i - count] = t

    return arr

def insertSortBin(arr):
    for i in range(1, len(arr)):
        t = arr[i]

        p = binSearch(t, 0, i-1, arr)

        for j in range(i, p, -1):
            arr[j] = arr[j-1]
        
        arr[p] = t
        print(arr)

    return arr

def binSearch(n, low, high, arr):

    if high <= low:
        if n >= arr[low]:
            return low + 1
        else:
            return low
    
    mid = (low + high) // 2

    if arr[mid] > n:
        return binSearch(n, low, mid-1, arr)
    else:
        return binSearch(n, mid+1, high-1, arr)

def myMin(arr):
    min = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min]:
            min = i
    return min

def bubbleSort(arr):
    for i in range(len(arr)):
        t = arr[i]
        k = myMin(arr[i:])
        
        arr[i] = arr[i+k]
        arr[i+k] = t
    return arr

def shellSort(arr):
    p = len(arr) // 2
    while p > 0:
        for i in range(p, len(arr)):
            j = i
            while j > 0 and arr[j] < arr[j-p]:
                t = arr[j]
                arr[j] = arr[j - p]
                arr[j - p] = t
                j -= p
        p //= 2
    return arr
