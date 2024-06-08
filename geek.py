b=[[2,43,5],[400,56,8]]
for i in b:
    f=i[:]
    k=max(i)
    i.remove(k)
    k=max(i)
    j=f.index(k)
    print(j,f)