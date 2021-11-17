
def mergeSort(arra,arrb):
    i = 0
    j = 0
    finalArr = []
    while i < len(arra)  and j < len(arrb) :
        if arra[i] < arrb[j]:
            finalArr.append(arra[i])
            i += 1
        else:
            finalArr.append(arrb[j])
            j += 1
    while i < len(arra):
        finalArr.append(arra[i])
        i += 1
    while j < len(arrb):
        finalArr.append(arrb[j])
        j += 1
    return finalArr
def Sort(arr):
    if len(arr) < 2 :
        return arr
    mid = len(arr)//2

    arr1 = []
    for index in range(0,mid ):
        arr1.append(arr[index])

    arr2 = []
    for index in range(mid,len(arr) ):
        arr2.append(arr[index]) 
        
    return mergeSort(Sort(arr1),Sort(arr2)) 



arr = [8,3,0,9,4,7,1,6,2,5]
print(Sort(arr))







