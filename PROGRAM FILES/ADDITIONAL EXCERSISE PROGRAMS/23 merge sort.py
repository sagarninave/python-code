#merge two array
#first subarray is arr[l.m]
#second subarray is arr[m+1..r]
def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m
    #create temp array
    L = [0]*(n1)
    R = [0]*(n2)
    #copy data to temp array l[] and r[]
    for i in range(0,n1):
        L[i]=arr[l+i]
    for i in range(0, n2):
        R[j] = arr[m + 1 + j]
        #merge the temp arrayblock into arr[l.r]
        i=0
        #initial index of first subarray
        j=0
        # initial index of second subarray
        k=l
        # initial index of Merge subarray
        while i<n1 and j<n2:
            if L[i]<=R[j]:
                arr[k] =L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        # copy the remaining element of l[i], if there are any
        while i< n1:
            arr[k] = L[i]
            i += 1
            k += 1
        # copy the remaining element of r[j], if there are any
        while j< n2:
            arr[k] = R[j]
            j += 1
            k += 1

# l is the left index and r is the right index of the sub array of the array to be sorted
def merge_sort(arr,l,r):
    if l<r:
        #same as(l+r)/2 but avoid overflow forlarge l and h
        m=(l+(r-1))/2
        #sort first and second halves
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)
#Drive code totest above
arr=[12,11,13,5,6,7]
n=len(arr)
print("given array is : ")
for i in range (n):
    print("%d"%arr[i])
    merge_sort(arr,0,n-1)
print("\n\n Sorted array is : ")
for i in range(n):
    print("%d"%arr[i])


