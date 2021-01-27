class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# 이진 탐색 트리에 데이터 넣기

class NoneMgmt:
    def __init__(self,head):
        self.head = head

    def insert(self,value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    # 이진 탐색 트리 탐색
    def search(self,value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right  

        return False

    # 이진 탐색 트리 삭제 코드 구현과 분석
    def delete(self,value):
        searched = False # 트리에 해당 노드가 없다.
        self.current_node = self.head # 삭제할 노드를 지칭하도록 할 것
        self.parent =self.head
        while self.current_node:
            if self.current_node.value == value: # 해당 노드 찾은 경우
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        
        if searched == False:  # 해당 노드 없다.
            return False
    
    ## 여기 부터는 삭제 Case 별로 코드 작성

    # Case 1 삭제할 Node가 Leaf Node인 경우
    # self.current_node 가 삭제할 Node, self.parent는 삭제할 node의 parent node인 형태
        if self.current_node.left == None and self.current_node.right ==None:
            if value < self.parent.value:
                self.parent.left =None
            else:
                self.parent.right = None
            del self.current_node
        
    # Case 2 : 삭제할 Node 가 child Node를 한 개 가지고 있을 경우
    # 왼쪽에 child node 갖고 있는 경우
        if self.current_node.left!= None and self.current_node.right ==None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
    
        elif self.current_node.left ==None and self.current_node.right != None:
            if value< self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
    
    # Case 3 : 삭제할 Node가 Child Node를 두 개 가지고 있는 경우
    # 3-1 :(삭제할 노드가 parent Node 왼쪽에 있을 때)

        if self.current_node.left !=None and self.current_node.right !=None: #case3
            if value<self.parent.value: #case 3-1
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left !=None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left=None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
    
    # 3-2 (삭제할 노드가 parent Node 오른쪽)
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left !=None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right !=None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.righte = self.current_node.right
    
        return True

    # 1 ~999 숫자 중에서 임의로 100개 추출해서 이진 탐색 트리에 입력,검색
    # 삭제 (random 라이브러리 활용)
    # ex) random.randint(0,99) : 0에서 99까지 숫자중 랜덤

import random

bst_nums = set() # 중복되는 수 제거하기 위해서
while len(bst_nums) !=100:
    bst_nums.add(random.randint(0,999))
#print(bst_nums)

#선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head=Node(500)
binary_tree =NoneMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

#입력한 100개의 숫자 검색
for num in bst_nums:
    if binary_tree.search(num) ==False:
        print("search faild",num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums) #인덱스 접근을 위해서
while len(delete_nums) !=10:
    delete_nums.add(bst_nums[random.randint(0,99)])

# 선택한 10개의 숫자를 삭제
for del_num in delete_nums:
    if binary_tree.delete(del_num)==False:
        print('delete failed',del_num)

