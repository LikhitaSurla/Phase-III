class Node:
    def __init__(self,data) -> None:
        self.data=data 
        self.left=None
        self.right=None
class BST:
    def addNode(self,root,value):
        newNode=Node(value)
        if root==None:
            root=newNode
        else:
            if root.data<value:
                if root.right == None:
                    root.right = newNode
                else:
                    self.addNode(root.right,value)
            else:
                if root.left == None:
                    root.left = newNode
                else:
                    self.addNode(root.left,value)
                    
        return root      
                
    def inorder(self,root):
        if root.left!=None:
            self.inorder(root.left)
        print(root.data,end="->")
        if root.right!=None:
            self.inorder(root.right)
            
    def preorder(self,root):
        print(root.data,end="->")
        if root.left!=None:
            self.preorder(root.left)
        if root.right!=None:
            self.preorder(root.right)
            
    def postorder(self,root):
        if root.left!=None:
            self.postorder(root.left)
        if root.right!=None:
            self.postorder(root.right)
        print(root.data,end="->")
       

    def levelorder(self,root):

        q=[root]
        while len(q)!=0:
            curr=q.pop(0)
            print(curr.data,end=" ")
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)
                


values=[16,9,25,4,10,8,83,15]
tree=BST()

root=tree.addNode(None,values[0])
for i in range(1,len(values)):
    tree.addNode(root,values[i])

tree.inorder(root)
print()
tree.preorder(root)
print()
tree.postorder(root)
print()
tree.levelorder(root)
