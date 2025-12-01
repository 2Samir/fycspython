class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        return self.stack.append(item)
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.stack.pop()
    def seek(self):
        return self.stack[-1]
    def is_empty(self):
        return self.stack==0
    def size(self):
        return len(self.stack)
    def dis(self):
        print(self.stack)
system = Stack()

while True:
    n=int(input("Enter 1:customer id, 2:cancle : "))
    if n==1:
        item = input("Enter details : ")
        system.push(item)
        system.dis()
    elif n==2:
        system.pop()
    else:
        print("Invalid input")