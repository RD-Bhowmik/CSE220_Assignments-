# class Node:
#     def __init__(self, elem, next = None):
#         self.elem = elem 
#         self.next = next 
        
# class singly_Circular:
#     def __init__(self,arr):
#         self.arr = arr 
#         self.head = None 
#         for i in self.arr :
#             new =  Node(i)
#             if self.head == None:
#                 self.head = new 
#                 self.head.next = self.head 
                
#             else : 
#                 cur = self.head 
#                 while cur.next is not self.head:
#                     cur = cur.next 
#                 cur.next = new 
#                 new.next = self.head 
                
#     # def dlt_idx(self,n):
#     #     count = 0 
#     #     cur = self.head 
#     #     if cur.elem == n : 
#     #         return count  
#     #     cur = cur.next  
#     #     while cur is not self.head: 
#     #         if cur.elem == n:
#     #             return count 
#     #         count +=1 
#     #         cur = cur.next 
            
#     def idx(self,n):
#         count  = 0
#         current = self.head
#         if current.elem == n:
#             return count
#         current = current.next
#         while current is not self.head:
#             if current.elem == n:
#                 return count
#             count+=1
#             current = current.next
    
#     def printing(self):
#         cur = self.head 
#         while cur.next is not self.head:
#             print(cur.elem)
#             cur = cur.next 
#             if cur.next is self.head :
#                 print(cur.elem)
                
                
        
                
# arr= [10,20,30,40,50]
# ll = singly_Circular(arr)
# ll.idx(30)
# ll.printing()

                    # Doubly circular linked list 
class Node:
    def __init__(self,elem,prev= None, next = None):
        self.elem = elem 
        self.prev = prev 
        self.next = next 
                    
class DCLL:
    def __init__(self,arr):
        self.arr = arr 
        self.head = None 
        for i in self.arr :
            new = Node(i)
            if self.head is None:
                self.head = new 
                self.head.next = self.head 
            else : 
                cur = self.head 
                while cur.next is not self.head:
                    cur.next = new 
                    new.prev = cur  
                    new.next = self.head 
                    self.head.prev = new 
                    
    def printing(self):
        cur = self.head 
        while cur is not self.head:
            print(cur.elem)
            cur = cur.next 
            # if cur.next is self.head:
            #     print(cur.elem)
                
arr = [100,200,300,405]
ll = DCLL(arr)
ll.printing()