


def InsertionSort(arr,i,j):
    if arr[i] > arr[j]:
        return
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    if j == 0:
        return
    InsertionSort(arr,j,j-1)
def Sort(arr):
    for i in range(len(arr)-1):
        if i == len(arr)-1:
            return
        j = i
        k = i+1
        while j >= 0:
            if arr[j] > arr[k]:
                temp = arr[j]
                arr[j] = arr[k]
                arr[k] = temp
            j -= 1
            k -= 1 


arr = [8,3,0,9,4,7,1,6,2,5]
Sort(arr)
print(arr)







