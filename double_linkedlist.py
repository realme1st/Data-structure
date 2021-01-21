class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.next = next
        self.prev = prev

class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head
    
    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    #연습문제 하기 위해 추가
    def search_from_head(self,data):
        if self.head ==None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False
    def search_from_tail(self,data):
        if self.head ==None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def insert_before(self,data,before_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node ==None:
                    return False

            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.next = node
            new.prev =before_new
            node.prev = new
            return True

double_linkedlist = NodeMgmt(0)

for data in range(1,10):
    double_linkedlist.insert(data)

double_linkedlist.desc()

# 연습문제 : 노드 데이터가 특정 숫자인 노드앞에 데이터 추가

node3= double_linkedlist.search_from_head(3)
if node3:
    print(node3.data)
else:
    print("no data")

node3 = double_linkedlist.search_from_tail(3)
if node3:
    print(node3.data)
else:
    print("no data")

double_linkedlist.insert_before(1.5,2)

double_linkedlist.desc()