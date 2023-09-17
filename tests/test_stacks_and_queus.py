import sys

sys.path.append("/Users/brendonericlucas/elementary_data_structures_in_python")
# replace with <path/to/containing_folder/elementary_data_structures_in_python>

from stacks_and_queues import Stack
from stacks_and_queues import Queue
from stacks_and_queues import QueueStack
from stacks_and_queues import StackQueue


def test_simple_stack():
    stack = Stack([])

    stack.push(1)
    stack.push(2)
    stack.push(3)

    first = 3
    second = 2
    third = 1

    assert first == stack.pop()
    assert second == stack.pop()
    assert third == stack.pop()

    assert stack.is_empty()


def test_simple_queue():
    queue = Queue([])

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    first = 1
    second = 2
    third = 3

    assert first == queue.dequeue()
    assert second == queue.dequeue()
    assert third == queue.dequeue()

    assert queue.is_empty()


def test_queue_stack():
    queue = Queue([])
    queue_stack = QueueStack()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    queue_stack.enqueue(1)
    queue_stack.enqueue(2)
    queue_stack.enqueue(3)

    assert queue_stack.dequeue() == queue.dequeue()
    assert queue_stack.dequeue() == queue.dequeue()
    assert queue_stack.dequeue() == queue.dequeue()

    assert queue_stack.is_empty()


def test_stack_queue():
    stack = Stack([])
    stack_queue = StackQueue()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack_queue.push(1)
    stack_queue.push(2)
    stack_queue.push(3)

    assert stack_queue.pop() == stack.pop()
    assert stack_queue.pop() == stack.pop()
    assert stack_queue.pop() == stack.pop()

    assert stack_queue.is_empty()
