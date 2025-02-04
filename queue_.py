queue =[]
def push():
    n = int(input("Enter the number you want to push :"))
    queue.append(n)
    print("The stack is : ",queue)

def pop():
    if not queue:
        print("t=The queue is empty..")
    else:
        queue.pop(0)
        print("The element is : ",queue)
        print("The queue is : ",queue)

while True:
    c = int(input("Enter 1 for push,2 for pop and 3 for break or exit : "))
    if c == 1:
        push()
    elif c ==2 :
        pop()
    elif c == 3:
        break
    
    else:
        print("Please choose the correct option ")