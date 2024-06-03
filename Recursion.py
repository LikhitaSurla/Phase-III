# Printing numbers 1 to 10 without loops

def fun(i,n):
    if i>n:
        return 
    else:
        print(i)
        fun(i+1,n)
n=int(input())
fun(1,n)
