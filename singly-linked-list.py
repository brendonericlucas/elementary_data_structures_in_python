class Node:
    def __init__(self, data, nextNode) -> None:
        self.data = data
        self.nextNode = nextNode

    def get_data(self) -> object:
        return self.data

    def next(self):
        return self.nextNode

    def update(self, node) -> None:
        self.nextNode = node


class LinkedList(Node):
    def __init__(self) -> None:
        self.head = Node(None, None)

    def initialize(self, array):
        currentNode = self.head
        for node in array:
            currentNode.nextNode = node
            currentNode = node

    def get_next_node(self, node) -> Node:
        return node.next()

    def get_data(self, node):
        return node.get_data()

    def remove_item_after_node(self, node) -> Node:
        if type(node) is tuple:
            node = node[0]
        temp = node.next()
        node.nextNode = temp.next()
        return temp

    def insert_item_after_node(self, at, node) -> Node:
        temp = at.next()
        at.nextNode = node
        node.nextNode = temp
        return node

    def get_penultimate(self) -> (Node, bool):
        currentNode = self.head
        nextNode = currentNode.next()
        has_penultimate = True
        if nextNode is None:
            has_penultimate = False
        else:
            while currentNode.next() is not None:
                if nextNode is not None:
                    if nextNode.next() is not None:
                        currentNode = currentNode.next()
                    nextNode = nextNode.next()
                else:
                    break
        return currentNode, has_penultimate

    def reverse(self):
        nextNode = self.head.next()
        if nextNode is None:
            pass
        elif nextNode.next() is None:
            pass
        else:
            tempLinkedList = LinkedList()
            currentOutNode = tempLinkedList.head
            currentInNode = self.get_penultimate()
            while True:
                tmp = self.remove_item_after_node(currentInNode)
                currentOutNode = tempLinkedList.insert_item_after_node(
                    currentOutNode, tmp
                )
                currentInNode, _continue = self.get_penultimate()
                if not _continue:
                    break
        temp = tempLinkedList.head.next()
        tempLinkedList.head = currentInNode
        self.head = currentInNode
        self.head.nextNode = temp

    def __repr__(self):
        currentNode = self.head
        strList = "[ "
        while currentNode.next() is not None:
            nextNode = currentNode.next()
            strList += "( {} )-->".format(nextNode.get_data())
            currentNode = nextNode
        strList = strList[0:-3] + "--\\\\ ]"
        return strList


if __name__ == "__main__":
    head = Node(None, None)
    # create additonal nodes, add them to the linked list
    nodes = [Node(i + 1, None) for i in range(10)]
    linked_list = LinkedList()
    linked_list.initialize(nodes)

    print(linked_list.__repr__())

    linked_list.reverse()
    print("Reversed List:")
    print(linked_list.__repr__())

