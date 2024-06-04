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
 