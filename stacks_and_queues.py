class Stack:
    def __init__(self, items) -> None:
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
        str_stack = "-----\n-----\n"
        if self.items:
            for item in self.items[-1::-1]:
                str_stack += "\n{0}\n-----\n".format(item)
            str_stack = str_stack + "-----\n\n"
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


class QueueStack:
    # implements a queue data structure using two stacks
    def __init__(self) -> None:
        self.s1 = Stack([])
        self.s2 = Stack([])

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        item = None

        while not (self.s1.is_empty()):
            self.s2.push(self.s1.pop())

        if not self.s2.is_empty():
            item = self.s2.pop()

        while not (self.s2.is_empty()):
            self.s1.push(self.s2.pop())

        return item

    def is_empty(self):
        return self.s1.is_empty()

    def __str__(self) -> str:
        str_queue_stack = "\n[QueueStack]\n{}\n<------->\n".format(self.s1.__str__())
        return str_queue_stack


class StackQueue:
    # implements a stack data structure using two queues
    pass


if __name__ == "__main__":
    stack = Stack([])
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

    queue_stack = QueueStack()
    print(queue_stack)
    queue_stack.enqueue(1)
    queue_stack.enqueue(2)
    queue_stack.enqueue(3)
    print(queue_stack)
    queue_stack.dequeue()
    print(queue_stack)
    queue_stack.dequeue()
    print(queue_stack)
    queue_stack.dequeue()
    print(queue_stack)
