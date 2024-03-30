def rotateArray(n:int, arr:[int]):
    count = arr[0]
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    arr[-1] = count
    return arr

n = 5
arr = [1,2,3,4,5]
print(rotateArray(n,arr))