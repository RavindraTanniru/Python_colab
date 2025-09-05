# arr =[-2,-3,-5,0,1,4,3,2,6,7]
# arr.sort()

def binary_search(arr,target):
    N =len(arr)
    L=0
    R=N-1
    while L<=R:
        M =L+((R-L)//2)
        if arr[M]==target:
            return M
        elif arr[M]<target:
            L =M+1
        else:
            R =M-1
    return -1
arr =[-2,-3,-5,0,1,4,3,2,6,7]
arr.sort()
a =binary_search(arr,7)
print(a)

