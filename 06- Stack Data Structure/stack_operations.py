stack = [12, 4, 88, 3, 22]


def push(stack):
    element = int(input("Enter element to push: "))
    stack.append(element)
    print(element, "pushed into stack.")


def pop(stack):
    if not stack:
        print("Stack is empty. Cannot pop.")
    else:
        print("Popped element:", stack.pop())


def display(stack):
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack elements are:", stack)


push(stack)
display(stack)
pop(stack)
display(stack)
