class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

iterator = head_node

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next
