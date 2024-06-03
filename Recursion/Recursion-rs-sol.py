# Passing data from Parent function to child function
def printSum(index, n, nums, result):
    if index == n:
        print("Sum is:", result)
        return 
 
    result += nums[index]
    #result = result + nums[index]
    printSum(index + 1, n, nums, result)
 
# Passing data from child function to Parent function
def printSum2(index, n, nums):
    if index == n:
        return 0 
    nextElementsSum = printSum2(index + 1, n, nums)
    return nextElementsSum + nums[index]
 
nums = [12, 34, 12, 5, 7]
n = len(nums)
result = printSum2(0, n, nums)
print("Sum is:", result)


#MaxElemnt

def findMaxInWay1(index, nums, n, result):
    if index == n:
        print("Max ele is:", result)
        return 
    if nums[index] > result:
        result = nums[index]
    findMaxInWay1(index + 1, nums, n, result)
 
nums = [12, 32, 11, 10]
result = findMaxInWay1(0, nums, len(nums), 0)
 
 
def findMaxInWay2(index, nums, n):
    if index == n - 1:
        return nums[index]
    nextGreater = findMaxInWay2(index + 1, nums, n)
    if nextGreater < nums[index]:
        return nums[index]
    return nextGreater 
 
nums = [12, 32, 11, 10]
result = findMaxInWay2(0, nums, len(nums))
print("Max ele:", result)


#Counting Vowels


def countVowelsWay1(word, index, n, result):
    if index == n:
        print("Vowels count is:", result)
        return 
    vowels = "aeiouAEIOU"
    if word[index] in vowels:
        result += 1 
    countVowelsWay1(word, index + 1, n, result)
 
 
word = "abcdeefuigh"
countVowelsWay1(word, 0, len(word), 0)
 
 
 
 
 
def countVowelsWay2(word, index, n):
    if index == n:
        return 0 
    nextVowelsCount = countVowelsWay2(word, index + 1, n)
    vowels = "aeiouAEIOU"
    if word[index] in vowels:
        nextVowelsCount += 1 
    return nextVowelsCount
 
 
word = "abcdeefuigh"
result = countVowelsWay2(word, 0, len(word))
print("Vowels count is:", result)