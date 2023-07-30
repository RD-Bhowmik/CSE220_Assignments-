class Node:
    def __init__(self,elem,prev=None, next= None):
        self.elem = elem 
        self.prev = prev 
        self.next = next 
        
class doubly:
    def __init__(self,arr):
        self.arr = arr 
        self.head = None 
        for i in range(len(self.arr)):
            new = Node(self.arr[i])
            if self.head is None:
                self.head = new 
            else : 
                cur = self.head 
                while cur.next is not None:
                    cur = cur.next 
                cur.next = new 
                new.prev = cur  
    
    def forward(self):
        cur = self.head 
        while cur is not None :
            print(cur.elem)
            cur = cur.next 
            
    def backword(self):
        cur = self.head 
        while cur.next is not None:
            cur = cur.next 
        while cur is not None :
            print(cur.elem)
            cur = cur.prev
            
    def find_idx(self,num):
        count = 0
        cur =  self.head 
        while cur is not None:
            if cur.elem == num:
                return (f"index number of {num} is {count}") 
            
            count +=1 
            cur = cur.next 
            
    def add(self,idx,num):
        new = Node(num)
        count= 0 
        cur = self.head 
        if (idx<0) or (idx>(len(self.arr))):
            print("invalid idx")
        while cur.next is not None:
            cur = cur.next
            count+=1
        
            
        if idx == 0:
            cur = self.head 
            self.head = new 
            self.head.next = cur  
            cur.prev = self.head  
        else : 
            count = 0 
            cur = self.head 
            while cur is not None :
                if idx == count+1:
                    break 
                cur = cur.next 
                count += 1 
            store = cur.next
            cur.next = new 
            new.next = store 
            # store.prev = new 
            new.prev = cur  
                 
                 
    def dlt(self,idx):
        count = 0 
        cur = self.head 
        while cur is not None:
            cur = cur.next 
            count +=1 
        if idx<0 or idx>5:
            print("invail index ")
            
        elif idx == count: 
            cur = self.head 
            while cur.next is not None:
                cur = cur.next 
                
            store = cur.prev 
            cur.prev = None 
            store.next = None 
        
        elif idx == 0 :
            self.head = self.head.next 
            cur = self.head.prev 
            self.head.prev = None
            cur.next = None 
            # self.head.next = None 
            
        else:     
            count = 0 
            cur = self.head 
            while cur is not None:
                if idx == count+1 :
                    break 
                cur =cur.next 
                count += 1
                
            store = cur.next.next 
            cur.next = store 
            # store.prev = cur 
        
           
        
            
        
        
        
    # def printing(self):
    #     cur = self.head 
    #     while cur is not None:                same as forward printing . 
    #         print(cur.elem)
    #         cur = cur.next 
        
#index= 0  1  2  3  4  5  6 
arr = [10,20,30,40,50,60]#100
ll = doubly(arr)
# ll.printing()
ll.find_idx(40)
print(ll.find_idx(40))
ll.add(6,100)
# ll.dlt(4)
ll.forward()
# ll.backword()

