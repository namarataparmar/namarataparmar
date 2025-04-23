class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
        print(f'{value} pushed to stack')
    
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            popped_value = self.stack.pop()
            print(f'{popped_value} popped from stack')
    
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print(f'Top element is {self.stack[-1]}')
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements are:", self.stack)

def stack_menu():
    stack = Stack()
    while True:
        print("\n--- Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if Stack is Empty")
        print("5. Display Stack")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value to push: "))
            stack.push(value)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.peek()
        elif choice == 4:
            if stack.is_empty():
                print("Stack is empty")
            else:
                print("Stack is not empty")
        elif choice == 5:
            stack.display()
        elif choice == 6:
            print("Exiting Stack program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the menu for stack
stack_menu()
