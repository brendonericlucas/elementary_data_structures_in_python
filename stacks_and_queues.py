class Stack:
    def __init__(self, items=[]) -> None:
        self.items = items

    def push(self, item):
        self.items.append(item)
        return self.items

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if self.items:
            return False
        else:
            return True

    def __str__(self) -> str:
        str_stack = ""
        if self.items:
            for item in self.items[-1::-1]:
                str_stack += str(item) + "\n_____" + "\n\n"
        else:
            str_stack = "\nEMPTY STACK\n"
        return str_stack


class Queue:
    def __init__(self, items=[]) -> None:
        self.items = items

    def enqueue(self, item):
        self.items = [item] + self.items
        return self.items

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        if self.items:
            return False
        else:
            return True

    def __str__(self) -> str:
        str_queue = ""
        if self.items:
            for item in self.items:
                str_queue += "| " + str(item) + " |"
            str_queue = "\n" + str_queue + "\n"
        else:
            str_queue = "\nEMPTY QUEUE\n"
        return str_queue


if __name__ == "__main__":
    stack = Stack()
    print(stack)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)

    queue = Queue()
    print(queue)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
