# -*- coding: utf-8 -*-
class stack:
    def __init__(self,Max):
        self.top = -1
        self.size = Max
        self.arr = [None]*Max
        
    def push(self,item):
        if(self.top == self.size-1):
            print("\n Stack is full !")
            
        else:
            self.top = self.top + 1
            self.arr[self.top] = item
            
    def pop(self):
        if (self.top == -1):
            print("The Stack is empty")
        else:
            x = self.arr[self.top]
            self.top = self.top - 1
            return x
        
    def display(self):
        if(self.top == -1):
            print("\n Stack is empty")
        else:
            print("\n Elements in the stack are:")
            for i in range(0,self.top + 1):
                print(self.arr[i],end = " ")
                
if __name__ == "__main__":
    obj =stack(5)
    obj.display()
    obj.push(90)
    obj.push(10)
    obj.push(20)
    obj.push(30)
    obj.display()
    print("\n The  1st deleted element is :",obj.pop())
    print("\n The  2nd deleted element is :",obj.pop())
    obj.display()
    obj.push(23)
    obj.display()
