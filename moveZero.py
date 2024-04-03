def moveZeros(n:int,a:[int]) ->[int]:

    smallest = -1
    for i in range(n):
        if a[i] == 0:
            smallest = i
            break
    
    if smallest == -1:
        return a
    

    for i in range(smallest+1, n):
        if a[i] != 0:
            a[smallest], a[i] = a[i], a[smallest]
            smallest += 1
    return a

n = 10
a = [1,2,3,0,22,0,3,4,0,6]
ans = moveZeros(n,a)
print(ans)