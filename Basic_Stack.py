
top=None
stack=[]

def Push(ele):
    global top
    stack.append(ele)
    if top==None:
        top=0
    else:
        top=top+1

def Pop():
    global top
    if top==None:
        print("Stack is empty")
    else:
        print(stack.pop())
        if top==0:
            top=None
        else:
            top=top-1

def status():
    if top==None:
        print("Stack is emity")
    else:
        print(stack)

while True:
    print("1:PUSH  2:POP  3:DISPLAY  4:EXIT")
    ch=int(input("Enter your choice:"))
    if ch==1:
        n=int(input("Enter element to be added"))
        Push(n)
    elif ch==2:
        Pop()
    elif ch==3:
        status()
    else:
        break



OUTPUT:
1:PUSH  2:POP  3:DISPLAY  4:EXIT
Enter your choice:1
Enter element to be added1
1:PUSH  2:POP  3:DISPLAY  4:EXIT
Enter your choice:1
Enter element to be added2
1:PUSH  2:POP  3:DISPLAY  4:EXIT
Enter your choice:1
Enter element to be added3
1:PUSH  2:POP  3:DISPLAY  4:EXIT
Enter your choice:3
[1, 2, 3]
1:PUSH  2:POP  3:DISPLAY  4:EXIT
Enter your choice:2
3
1:PUSH  2:POP  3:DISPLAY  4:EXIT
Enter your choice:4
