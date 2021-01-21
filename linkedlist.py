#간단한 링크드 리스트 예

# 1. 노드 구현
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# 다른 방법
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

# 2. Node와 Node 연결하기 (포인터 활용)

node1=Node(1)
node2=Node(2)
node1.next = node2
head = node1 # 노드 맨 앞을 알아야된다.

# 3. 링크드 리스트로 데이터 추가하기
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def add(data):
    node =head
    while node.next: # node의 next가 있다면
        node = node.next
    # node next가 없다면
    node.next = Node(data)

# 링크드 리스트 데이터 출력하기
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)
