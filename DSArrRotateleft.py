#left rotate the array by 1 
# first obv make a fun and init loop

"""Iteration 1: i = 1
arr[i - 1] becomes arr[i], so arr[0] becomes 1.
Iteration 2: i = 2
arr[i - 1] becomes arr[i], so arr[1] becomes 4.
Iteration 3: i = 3
arr[i - 1] becomes arr[i], so arr[2] becomes 1.
Iteration 4: i = 4
arr[i - 1] becomes arr[i], so arr[3] becomes 5.
After this loop, the array becomes [1, 4, 1, 5, 5]. """

def LrotateArray(n:int, arr:[int]):
    count = arr[0]
    for i in range(1,len(arr)):
        
        arr[i-1] = arr[i]
    arr[-1] = count
    return arr

n = 5
arr = [1,2,3,4,5]
print(LrotateArray(n,arr))