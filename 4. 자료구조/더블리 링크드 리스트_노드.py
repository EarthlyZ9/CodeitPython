class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    # __init__, find_node_at, fine_node_with_data, __str__메소드는 싱글리 링크드 리스트와 동일

    def __init__(self):
        self.head = None
        self.tail = None

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 연산: 삭제"""
        deleted_data = node_to_delete

        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return deleted_data.data

    def append(self, data):
        """더블리 링크드 리스트 연산: 추가"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:  # 이미 데이가 존재할 때
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, previous_node, data):
        """더블리 링크드 리스트 연산: 삽입"""
        new_node = Node(data)

        # 맨 뒤에 삽입할 때
        if previous_node.next is None:
            new_node.prev = previous_node
            previous_node.next = new_node
            self.tail = new_node
        else:  # 중간에 삽입할 때
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def prepend(self, data):
        """더블리 링크드 리스트 연산: 맨 앞에 삽입"""
        # 코드를 쓰세요
        new_head_node = Node(data)
        if self.head is None:  # 리스트가 비어있는 경
            self.head = new_head_node
            self.tail = new_head_node
        else:
            new_head_node.next = self.head
            self.head.prev = new_head_node
            self.head = new_head_node

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

    def __str__(self):
        res_str = "|"
        iterator = self.head

        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next

        return res_str


# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 새로운 노드 5개 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)

# tail 노드 뒤에 노드 삽입
tail_node = my_list.tail  # 4 번째(마지막)노드를 찾는다
my_list.insert_after(tail_node, 5)  # 4 번째(마지막)노드 뒤에 노드 추가
print(my_list)
print(my_list.tail.data)  # 새로운 tail 노드 데이터 출력

# 링크드 리스트 중간에 데이터 삽입
node_at_index_3 = my_list.find_node_at(3)  # 노드 접근
my_list.insert_after(node_at_index_3, 3)
print(my_list)

# 링크드 리스트 중간에 데이터 삽입
node_at_index_2 = my_list.find_node_at(2)  # 노드 접근
my_list.insert_after(node_at_index_2, 2)
print(my_list)
