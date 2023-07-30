class Node:
    def __init__(self,value,next = None,prev=None):
        self.value =  value
        self.next = next
        self.prev = prev

class Doubly_linkedlist:
    def __init__(self,arr):
        self.arr = arr
        self.head = None
        for i in range(len(self.arr)):
            new_node = Node(self.arr[i])
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = new_node
                new_node.prev = current

    def print_forward(self):
        current =  self.head
        while current is not None:
            print(current.value)
            current = current.next

    def print_backward(self):
        current = self.head
        while current.next is not None:
            current = current.next
        while current is not None:
            print(current.value)
            current = current.prev

    def idx_of_elem(self,n):
        count = 0
        current = self.head
        while current is not None:
            if current.value == n:
                return count
            count += 1
            current = current.next

    def add_elem(self,idx,n):
        new_node = Node(n)
        count = 0
        current = self.head
        if idx<0 or idx>4:
            print("invalid idx")
        while current is not None:
            current = current.next
            count+=1
        if idx == 0 :
            current = self.head
            self.head = new_node
            self.head.next = current
            current.prev = self.head
        else:
            i = 0
            current = self.head
            while current is not None:
                if idx == i+1:
                    break
                current = current.next
                i+=1
            current2 = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = current2
            current2.prev = new_node

    def delete_Idx(self,index):
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count+=1
        if index == count:
            current = self.head
            while current.next is not None:
                current = current.next
            current2 = current.prev
            current.prev = None
            current2.next = None

        elif index == 0:
            current = self.head.next   #self.head  = self.head.next (2 line er shortcut)
            self.head = current
            current = self.head.prev
            self.head.prev = None
            current.next = None

        else:
            count = 0
            current = self.head
            while current is not None:
                if index == count+1:
                    break
                current = current.next
                count+=1
            current2 = current.next.next
            current.next = current2
            current2.prev = current





arr = [10,20,30,40,50]
q = Doubly_linkedlist(arr)
# q.print_forward()
# q.print_backward()
# q.idx_of_elem(30)
# print(q.idx_of_elem(30))
# q.add_elem(3,1000)
q.delete_Idx(4)
q.print_forward()