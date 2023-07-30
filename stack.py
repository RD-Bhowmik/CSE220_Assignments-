class stack:
    def __init__(self):
        self.lst = [0]*6
        self.top = -1 
        
    def push(self,n):
        if self.top == len(self.lst)-1:
            print("Stack over-flow")
            
        else :
            self.top += 1 
            self.lst[self.top]=n  
            
    def peek(self):
        if self.top == -1:
            print("stack is empty")
        else:
            return self.lst[self.top]
        
    def pop(self):
        if self.top == -1 :
            print("stack underflow")
            return "stack under flow"
        else :
            n = self.lst[self.top]
            self.lst[self.top]=0
            self.top ==-1 
            return n    
        
s = stack()
s.push(10)
s.push(20)
s.push(100)
b = s.peek()
print(b)
a = s.pop()
print(a)
# print(s)