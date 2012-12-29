import math

class CNode:
    left , right, data = None, None, 0
  
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class CBOrdTree:
    def __init__(self):
        self.root = None
    
    def addNode(self, data):
        return CNode(data)

    def insert(self, root, data):
        if root == None:
            return self.addNode(data)
        else:
            if data <= root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
            return root
        
    def lookup(self, root, target):
        if root == None:
            return 0
        else:
            if target == root.data:
                return 1
            else:
                if target < root.data:
                    return self.lookup(root.left, target)
                else:
                    return self.lookup(root.right, target)
        
    def minValue(self, root):
        while(root.left != None):
            root = root.left
        return root.data

    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            return max(ldepth, rdepth) + 1
            
    def size(self, root):
        if root == None:
            return 0
        else:
            return self.size(root.left) + 1 + self.size(root.right)

    def printTree(self, root):
        # prints the tree path
        if root == None:
            pass
        else:
            self.printTree(root.left)
            print(root.data)
            self.printTree(root.right)

    def printpathtoroot(self, root, target, res):
        if root == None:
            pass
        else:
            if target == root.data:
                 return self.getchilden(root, res)
            else:
                if target < root.data:
                    # left side
                    res.append(root.data)
                    self.printpathtoroot(root.left, target, res)
                else:
                    # right side
                    res.append(root.data)
                    self.printpathtoroot(root.right, target, res)


    def getchilden(self, root, res):
       if root == None:
            return res
       else:
            self.getchilden(root.left, res)
            res.append(root.data)
            self.getchilden(root.right, res)
   

    def printRevTree(self, root):
        if root == None:
            pass
        else:
            self.printRevTree(root.right)
            print(root.data)
            self.printRevTree(root.left)

if __name__ == "__main__":
    BTree = CBOrdTree()
    lists=[11650, 14430, 15978, 18927, 19114, 19434, 19843]
    res= []
    lists.sort()
    
    mid= int(math.floor(len(lists)/2))
    root = BTree.addNode(lists[mid])
    ptr= int(math.floor(mid/2))
    while ptr>0:
        BTree.insert(root, lists[ptr])
        BTree.insert(root, lists[ptr+1+mid])
        cur_ptr= ptr
        ptr=ptr/2
        
    BTree.insert(root, lists[cur_ptr-1])  
    BTree.insert(root, lists[cur_ptr+1])  
    BTree.insert(root, lists[cur_ptr+mid])  
    BTree.insert(root, lists[cur_ptr+mid+2])  
    print
    BTree.printTree(root)

    data= int(raw_input("print path from root to value: "))
    BTree.printpathtoroot(root, data, res)
    
    print(res)
    
