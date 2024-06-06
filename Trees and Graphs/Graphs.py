def BFS(start,graph):
    # Queue is used
    visited=[start]
    Q=[start]
    while len(Q)>0:
            curr=Q.pop(0)
            for i in graph[curr]:
                if i not in visited:
                    Q.append(i)
                    visited.append(i)
    return visited
        
def DFS(start,graph,visited=None):
        # Stack  is used
        if visited==None:
            visited=[]
        visited.append(start)
        for n in graph[start]:
            if n not in visited:
                DFS(n,graph,visited)
        return visited
            
            
graph={"A":["B","C"],  
       "B":["A","C","D"],
       "C":["A","B","E"],
       "D":["B","E"],
       "E":["C","D"]
   }
   
res=BFS("C",graph)
res=DFS("E",graph)
print(res)

