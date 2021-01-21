#리스트 변수로 enqueue, dequeue 기능 구현

queue_list=list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data=queue_list[0] # 지칭
    del queue_list[0]  #맨 앞부분 삭제
    return data

