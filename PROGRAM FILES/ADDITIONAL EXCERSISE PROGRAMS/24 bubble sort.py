#program for bubble sort
def bubble_sort(arr):
    n=len(arr)
    #traverse thorugh all array element
    for i in range(n):
        #last i element already in place
        for j in range(0,n-i-1):
            #traverse the array from 0 to n-i-1
            #swap if the element found o=is greaer
            #than the next element
            if arr[i] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# drive code to test above
arr=[64,34,25,12,22,11,90]
bubble_sort(arr)
print("sorted array is : ")
for i in range (len(arr)):
    print("%d" %arr[i])