stack =[]
def push():
    n = int(input("Enter the number:"))
    stack.append(n)
    print("the elements are after push:",stack)
def pop():
    e= stack.pop()
    print("After push the element is: ",e )
    print("After pop the stack is : ",stack)


while True:
    print("Enter 1 for push & 2 for pop & 3 for exit : ")
    c = int(input("Enter your choice:"))
    if c == 1:
        push()
    elif c == 2:
         pop()
    elif c == 3:
           break
    else:
            print("please choose a correct option")
