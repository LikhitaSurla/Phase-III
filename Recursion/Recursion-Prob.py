
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





