n =5
for i in range(1,n+1):
    print("*" * i)


n = 5

for i in range(n,0,-1):
    print("*" * i)


rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))


n =5
for i in range(1,n+1):
    print(" " * (n-i) + "*" * (2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i) + "*"*(2*i-1))
    
    
n =5
for i in range(n):
    print("*"*n)