
# Printing numbers 1 to 10 without loops

def fun(i,n):
    if i>n:
        return 
    else:
        print(i)
        fun(i+1,n)
n=int(input())
fun(1,n)

#or


def fun(i,n):
    if i<=n:
        print(i)
        fun(i+1,n)
n=int(input())
fun(1,n)

# Guess the outputs from code snippets using Recursice stack

def printThiis(i,n):
    if i>=n:
        print("Base condition got hit")
        return
    print("Ending line",i)
    for j in range(1,i):
        print(j)
    printThiis(i+1,n)
    print("starting line",i)
printThiis(1,5)
    

def printThis(position):
    print("Leaving here",position)
    if(position==0):
        print("Base condition got hit")
        return
    if position%2==1:
        print("Even positin:",position)
    else:
        print("odd position",position)
    printThis(position-1)
    for index in range(position,-1,-1):
        print("Index is",index)
    print("Entering here",position)
printThis(4)



#sum of elements
# Passing data from Parent function to child function

def total(i,n,nums,sums):
   
    if i<n:
        sums=sums+nums[i]
        total(i+1,n,nums,sums)
    else:
        print(sums) 
    
nums=[15,21,85,-50]
n=len(nums)
sums=0
total(0,n,nums,sums)

# Passing data from child function to Parent function
def printSum2(index, n, nums):
    if index == n:
        return 0 
    nextElementsSum = printSum2(index + 1, n, nums)
    return nextElementsSum + nums[index]
 
nums = [15, 21, 85, -50]
n = len(nums)
result = printSum2(0, n, nums)
print(result)
 

#max element - backtracking

def maxEle(i,n,nums):
    if i<n:
        return max(nums[i],maxEle(i+1,n,nums))
    else:
        return 0
    
    
nums=[12,450,2300,78]
n=len(nums)
print(maxEle(0,n,nums))  


#max element - recursion

def maxEle(i,n,nums,maxi):
    if i<n:
        if nums[i]>maxi:
            maxi=nums[i]
        maxEle(i+1,n,nums,maxi)
    else:
        print(maxi)
    pass
nums=[12,45,23,78]
n=len(nums)
maxi=nums[0]
maxEle(0,n,nums,maxi)



#min element
def minEle(i,n,nums,mini):
    if i<n:
        if nums[i]<mini:
            mini=nums[i]
        minEle(i+1,n,nums,mini)
    else:
        print(mini)
    pass
nums=[12,45,23,78]
n=len(nums)
mini=nums[0]
minEle(0,n,nums,mini)


def minEle(i,n,nums):
    if i<n:
        return min(nums[i],minEle(i+1,n,nums))
    else:
        return nums[0]
    
    
nums=[12,450,2300,78]
n=len(nums)
print(minEle(0,n,nums))  



def findVowels(i,n,s,count,li):
    if i==n:
        print(count)
        return count
    else:
        if s[i] in li:
            count+=1
        return findVowels(i+1,n,s,count,li)
s="likhitaa"
n=len(s)
count=0
li=['A','E','I','O','U','a','e','i','o','u']
print(findVowels(0,n,s,count,li))


