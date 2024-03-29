import sys

def secOrdElement(n:int, a: [int]) -> [int]:
   
    secLargest = secondLargest(n,a)
    secSmallest = secondSmallest(n,a)
    print(secLargest, secSmallest)
    return [secLargest,secSmallest]
    pass

def secondLargest(n:int, a:[int])->  [int]:
    largest = a[0]
    secondlargest = a[-1]

    for i in range(0,n):
        if a[i] > largest:
            secondlargest = largest
            largest = a[i]
        if a[i] < largest and a[i] > secondlargest:
            secondlargest = a[i]
    return secondlargest

def secondSmallest(n:int, a:[int]) ->  [int]:
    smallest = a[0]
    secondsmallest = sys.maxsize

    for i in range(0,n):
        if a[i] < smallest:
            secondsmallest = smallest
            smallest = a[i]
        if a[i] != smallest and a[i]<secondsmallest:
            secondsmallest = a[i] 
    return secondsmallest

n = 5
a = [12,33,44,55,66]   
secOrdElement(n,a)