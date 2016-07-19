def partition(A,l,r):
    global compare
    compare += r - l
    middle = (l+r)/2
    
    if  A[r] >= A[middle] >= A[l] or A[l] >= A[middle] >= A[r]:#middle is the true median
        A[l], A[middle] = A[middle], A[l]
        p = A[l]
    elif A[l] >= A[r] >= A[middle] or A[middle] >= A[r] >= A[l]:#r is the median value
        A[r], A[l] = A[l], A[r]
        p = A[l]
    else:
        p = A[l]
    
    
    i = l + 1
    for j in range(l+1,r+1):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]
    return i-1


def QuickSort(A, head, tail):
    global compare 
    
    if head < tail:
        i = partition(A,head,tail)
        QuickSort(A,head,i-1)
        QuickSort(A,i+1,tail)
    else:
        return


f = open("./QuickSort_2.txt","r")

data = []
for l in f.readlines():
    data.append(int(l))

print len(data)

global compare 
compare = 0

QuickSort(data,0,len(data)-1)

print compare
