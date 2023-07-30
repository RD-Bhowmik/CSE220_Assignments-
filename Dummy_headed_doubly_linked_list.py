class Node:
    def __init__(self,elem , prev = None, next = None):
        self.elem = elem 
        self.prev = prev 
        self.next = next 
        
class DHDLL:
    def __init__(self, arr):
        self.arr = arr 
        self.head = Node(None)
        for i in self.arr :
            new = Node(i)
            cur = self.head 
            while cur.next is not None:
                cur = cur.next 
            cur.next = new 
            new.prev = cur  
        
    def printing(self):
        cur = self.head 
        while cur is not None:
            print(cur.elem)
            cur = cur.next 
            
arr = [10,20,30,40]
ll = DHDLL(arr)
ll.printing()

        