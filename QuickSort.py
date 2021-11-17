
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partiation(nums,start,end):
    pivit = nums[end]
    pIndex = start
    index = start
    while index < end:
        if nums[index] < pivit:
            swap(nums,index,pIndex)
            pIndex += 1
        index += 1
    swap(nums,index,pIndex)
    return pIndex

def quickSort(nums,start,end):
    if start >= end:
        return
    pIndex = partiation(nums,start,end)
    quickSort(nums,start,pIndex-1)
    quickSort(nums,pIndex+1,end)



arr = [8,3,0,9,4,7,1,6,2,5]

quickSort(arr,0,len(arr)-1)

print(arr)







