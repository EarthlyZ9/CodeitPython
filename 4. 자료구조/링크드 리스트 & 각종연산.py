class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def delete_after(self, previous_node):
        """링크드 리스트 연산: 삭제"""
        data = previous_node.next.data  # 파이썬에서는 삭제된 요소를 리턴해주는 것이 관습임
        # 지우려는 노드가 tail 노드일 때
        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        else:  # 지우려는 노드가 중간에 있을 때
            previous_node.next = previous_node.next.next

        return data

    def pop_list(self):
        """head 노드 지우기"""
        head_node = self.head
        if self.head is self.tail:  # 노드가 하나 밖에 없을 때
            self.head = None
            self.tail = None
        else:  # 노드가 두 개 이상일 때
            self.head = self.head.next

        return head_node.data

    def insert_after(self, previous_node, data):
        new_node = Node(data)
        if previous_node == self.tail:
            """맨 끝에 새로운 노드 삽입할 때"""
            self.tail.next = new_node
            self.tail = new_node
        else:
            """중간에 삽입할 때"""
            new_node.next = previous_node.next
            previous_node.next = new_node

    def prepend(self, data):
        """맨 앞에 새로운 노드 삽입"""
        new_node = Node(data)
        if self.head is None:  # 리스트가 비었을 때
            self.head = new_node
            self.tail = new_node
        else:  # 리스트에 요소가 하나 이상 있을 때
            new_node.next = self.head
            self.head = new_node

    def find_node_at(self, index):
        """링크드 리스트 연산: 접근"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next
            # for 문이 끝나면 원하는 index를 가리키고 있을 것임.

        return iterator

    def fine_node_with_data(self, data):
        """주어진 데이터를 갖고 있는 노드 리턴, 리스트에 없으면 None 리턴"""
        iterator = self.head

        while iterator is not None:
            if iterator.data == data:
                return iterator

            iterator = iterator.next
        return None

    def append(self, data):
        """링크드 리스트 연산: 추가"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        res_str = "|"
        iterator = self.head

        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next

        return res_str


my_list = LinkedList()
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)

node_2 = my_list.find_node_at(2)
my_list.delete_after(node_2)

print(my_list)

second_to_last_node = my_list.find_node_at(2)
print(my_list.delete_after(second_to_last_node))

print(my_list)
