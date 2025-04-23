class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
        print(f'{value} added to queue')
    
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            dequeued_value = self.queue.pop(0)
            print(f'{dequeued_value} removed from queue')
    
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print(f'Front element is {self.queue[0]}')
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue elements are:", self.queue)

def queue_menu():
    queue = Queue()
    while True:
        print("\n--- Queue Menu ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Check if Queue is Empty")
        print("5. Display Queue")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value to enqueue: "))
            queue.enqueue(value)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.peek()
        elif choice == 4:
            if queue.is_empty():
                print("Queue is empty")
            else:
                print("Queue is not empty")
        elif choice == 5:
            queue.display()
        elif choice == 6:
            print("Exiting Queue program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the menu for queue
queue_menu()
