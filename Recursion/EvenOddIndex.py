#  write a python program to print all even indexed 
# elements in both left to right and right to left manner 
# using recursion.

# [10, 11, 12, 13, 14, 15]
# 	 0.  1.  2.   3.  4.  5 
# 	even indices: 0, 2, 4 
# 	odd indices: 1, 3, 5 
 
def printLeftToRight(index, nums, n):
	if index == n:
		return 
 
	if index % 2 == 0:
		print(nums[index])
	printLeftToRight(index + 1, nums, n)
 
def printLeftToRightBetterOne(index, nums, n):
	if index >= n:
		return 
 
	print(nums[index])
	printLeftToRightBetterOne(index + 2, nums, n)
 
def printRightToLeftBetterOne(index, nums, n):
	if index >= n:
		return 
 
	printLeftToRightBetterOne(index + 2, nums, n)
	print(nums[index])
	printLeftToRight(0, nums, len(nums))
 
 
 
def printRightToLeftInReverseManner(index, nums, n):
	if index < 0:
		return 
	print(nums[index])
	printRightToLeftInReverseManner(index - 2, nums, n)
 
 
nums=[12,85,21,65]
n = len(nums)
if n % 2 == 0:
	printRightToLeftInReverseManner(n - 2, nums, n)
else:
	printRightToLeftInReverseManner(n - 1, nums, n)
 
