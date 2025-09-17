'''
def gcd(a,b):
    while b !=0:
        a,b =b,a%b
    return a
print(gcd(12,18))



def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

print(lcm(12, 18))  





# Step 1: Function to calculate GCD of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Replace a with b, b with a%b
    return a

# Step 2: Function to calculate LCM of two numbers using GCD
def lcm(a, b):
    return (a * b) // gcd(a, b)

# Step 3: Function to calculate LCM of a list of numbers
def lcm_of_list(nums):
    result = nums[0]        # Start with the first number
    for n in nums[1:]:      # Loop through the rest of the numbers
        result = lcm(result, n)  # Compute LCM of result so far and current number
    return result

# Step 4: Test the function
numbers = [4, 6, 8]
print("LCM of", numbers, "is", lcm_of_list(numbers))  # Output: 24


import math
from functools import reduce

# Function to calculate LCM of two numbers
def lcm(a, b):
    return (a * b) // math.gcd(a, b)  # Use math.gcd instead of custom gcd

# Function to calculate LCM of a list of numbers
def lcm_of_list(nums):
    return reduce(lcm, nums)  # Reduce applies lcm pair by pair automatically

# Example
numbers = [4, 6, 8]
print("LCM of", numbers, "is", lcm_of_list(numbers))  # Output: 24




import math

def factors(n):
    result = set()  # Use set to avoid duplicates
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return sorted(result)

print(factors(36))  # Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]


def decimal_to_binary(n):
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n = n // 2
    binary.reverse()
    return ''.join(binary)

print(decimal_to_binary(13))  # Output: 1101



def is_prime(n):
    if n<=1:
        return False
    elif n%2==0 or n%3==0:
        return False
    else:
        return True
    
print(is_prime(7))


import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Check up to √n
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(25))  # False
print(is_prime(49))  # False



def decToBinary(n):
    binArr=[]
    while n>0:
        bit =n%2
        binArr.append(str(bit))
        n =n//2
        
    binArr.reverse()
    return "".join(binArr)

print(decToBinary(12))


def decToBinary(n):
    bin =""
    while n>0:
        bit =n&1
        bin +=str(bit)
        n//=2
    
    return bin[::-1]


print(decToBinary(12))


import math 

def decToBinary(n):
    return bin(n)[2::]

print(decToBinary(0))


def gcd(a,b):
    while b!=0:
        a,b =b,a%b
    return a
def lcm(a,b):
    return (a*b) // gcd(a,b)
a =gcd(20,28)
print(a)

a =lcm(10,5)

print(a)



import math 

def lcm(a,b):
    return math.lcm(a,b)

print(lcm(10,5))



def square_num(n):
    return n**2

print(square_num(2))



def factors(n):
    my_list =[]
    i =1
    while i<=n:
        if n%i==0:
            my_list.append(i)
        i =i+1
    return my_list

print(factors(10))

        


def is_prime(n):
    
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True
a =is_prime(25)
print(a)
        



def modmul(a, b, M):
    
    return (a % M) * (b % M) % M


a = 5
b = 3
M = 11
print(modmul(a, b, M))


def mod(a,b,M):
    return (a*b)%M

print(mod(5,3,11))




def ncr(n,r):
    
    
    if r>n:
        return 0
    if r==0 or r==n:
        return 1
    return ncr(n-1,r-1)+ncr(n-1,r)

a =ncr(5,2)
print(a)
'''


def ncr(n,r):
    
    if r>n:
        return 0
    if r==0 or r==n:
        return 1
    
    