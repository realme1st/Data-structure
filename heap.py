class Heap: # 이 코드는 Max heap을 구현
    def __init__(self,data):
        self.heap_array = list()
        self.heap_array.append(None) # 인덱스를 1부터 시작하기 위해 0은 None으로
        self.heap_array.append(data)


    def move_up(self,inserted_idx):
        if inserted_idx <=1: # insert 가는 위치가 root node 인 경우 
            return False
        
        parent_idx = inserted_idx //2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False


    def insert(self,data):
        if len(self.heap_array) ==0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        
        inserted_idx = len(self.heap_array)-1

        # insert 노드가 부모보다 큰 경우 바꿔주는 것
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx],self.heap_array[parent_idx] = self.heap_array[parent_idx],self.heap_array[inserted_idx]
            inserted_idx = parent_idx

        return True
    def move_down(self,poped_idx):
        left_child_poped_idx = poped_idx * 2
        right_child_poped_idx = poped_idx *2 +1

        #case1 : 왼쪽 자식 노드도 없을 때
        if left_child_poped_idx >= len(self.heap_array):
            return False
        #case2: 오른쪽 자식 노드만 없을 때
        elif right_child_poped_idx >=len(self.heap_array):
            if self.heap_array[poped_idx] <self.heap_array[left_child_poped_idx]:
                return True
            else:
                return False
        # case3 : 왼쪽 오른쪽 자식 노두 모두 있을 때
        else:
            if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx]:
                if self.heap_array[poped_idx] <self.heap_array[left_child_poped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[poped_idx]<self.heap_array[right_child_poped_idx]:
                    return True
                else:
                    return False
                    

    # root 에 있는 data를 빼는 코드
    def pop(self):
        if len(self.heap_array) <=1:
            return None
        
        returned_data =self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1] #맨 끝에 있는 걸 root로
        del self.heap_array[-1]
        poped_idx = 1

        while self.move_down(poped_idx):
            left_child_poped_idx = poped_idx * 2
            right_child_poped_idx = poped_idx *2 +1

            #case2: 오른쪽 자식 노드만 없을 때
            if right_child_poped_idx >=len(self.heap_array):
                if self.heap_array[poped_idx] <self.heap_array[left_child_poped_idx]:
                    self.heap_array[poped_idx],self.heap_array[left_child_poped_idx] = self.heap_array[left_child_poped_idx],self.heap_array[poped_idx]
                    poped_idx =left_child_poped_idx
            # case3 : 왼쪽 오른쪽 자식 노두 모두 있을 때
            else:
                if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx]:
                    if self.heap_array[poped_idx] <self.heap_array[left_child_poped_idx]:
                        self.heap_array[poped_idx],self.heap_array[left_child_poped_idx] = self.heap_array[left_child_poped_idx],self.heap_array[poped_idx]
                        poped_idx =left_child_poped_idx

                else:
                    if self.heap_array[poped_idx]<self.heap_array[right_child_poped_idx]:
                        self.heap_array[poped_idx],self.heap_array[right_child_poped_idx] = self.heap_array[right_child_poped_idx],self.heap_array[poped_idx]
                        poped_idx = right_child_poped_idx
        return returned_data

# Test  
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)

heap.pop()
print(heap.heap_array)

