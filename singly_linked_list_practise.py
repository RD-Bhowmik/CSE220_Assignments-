# arr = [10,20,30,40,50]
# for i in range(len(arr)-1):
#     arr[i] = arr[i+1]
# arr[len(arr)-1] = 0 
# print(arr)


                                    # Linked List ----> Singly Linked List 
                                    

class Node: 
    def __init__(self, val , next= None ):
        self.val  = val 
        self.next = next 
        
class singly:
    def __init__(self, arr):
        self.arr = arr  
        self.head =  None  
        for i in range(len(self.arr)):
            newNode = Node(self.arr[i])
            if self.head is None:
                self.head = newNode
            else: 
                current = self.head 
                while current.next is not None :
                    current = current.next 
                    
                current.next = newNode 
                
    def find_idx(self,num):
        count = 0 
        cur = self.head 
        while cur is not None :
            if cur.val == num:
                return (f"index number of {num} is {count}")  
            else : 
                cur = cur.next 
                count +=1 
                
    def insert_head(self,number):
        newNode  = Node(number)
        current = self.head 
        self.head = newNode 
        self.head.next = current 
                
    def insert_tail(self,x):
        new = Node(x)
        cur = self.head 
        while cur.next is not None :
            cur = cur.next 
        cur.next = new 
        
    def insert_specific(self,idx,num):
        new = Node(num)
        if idx == 0:
            cur = self.head 
            self.head = new 
            self.head.next = cur 
        else:
            count = 0 
            cur = self.head 
            while cur is not None: 
                if idx == count+1:
                    break 
                cur = cur.next 
                count += 1
            store = cur.next 
            cur.next = new 
            cur = cur.next 
            new.next = store 
            
    def dlt(self,idx):
        if idx == 0:
            cur = self.head.next 
            self.head.next = None 
            self.head = cur  
        else : 
            count = 0 
            cur = self.head 
            while cur is not None:
                if idx == count+1:
                    break 
                cur = cur.next 
                count += 1 
            
            store = cur.next.next 
            cur.next = store 
            
    def reverse_lst(self):
        prev = None 
        next = None
        cur = self.head 
        while cur is not None:
            next = cur.next 
            cur.next = prev 
            prev = cur 
            cur = next 
        self.head = prev 
        
    def printing(self):
        current = self.head
        while current is not None :
            print(current.val)
            current =current.next
                 
                        
arr = [10,20,30,40,50]
ll = singly(arr)
print(ll.find_idx(50))
ll.insert_head(1000)
ll.insert_tail(200)
ll.insert_specific(7,550)
ll.dlt(7)
# ll.printing()
ll.reverse_lst()
ll.printing()

