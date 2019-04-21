class Stack:
    
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        if self.items:
            return self.items.pop()
        print('Stack is empty')
    
    # show the next value that is ready to be popped  
    def peek(self):
        if self.items:
            return self.items[-1] # last item in the list
        print('Stack is empty')
        
    def size(self):
        return len(self.items)
        
    def is_empty(self):
        return (self.items == [])
print('Using local Stack class')