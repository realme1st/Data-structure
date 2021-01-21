#리스트 변수로 스택을 다루는 pop,push 구현

stack_list =list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data
