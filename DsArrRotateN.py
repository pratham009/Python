def rotateD(arr:[int], k:int):
    k = k%len(arr)

    reverse(arr, 0, k-1)
    reverse(arr, k, len(arr)-1 )
    reverse(arr, 0, len(arr)-1)
    return arr

def reverse(arr:[int], start:int, end:int):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1 
        end -= 1 

arr = [12,22,33,4,5,44]
k = 3
print(rotateD(arr,k))