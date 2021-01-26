# 1. 해쉬함수 key % 8
# 2. 해쉬 키 생성 : hash(data)

hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data,value):
    index_key = get_key(data) # 별도로 key 저장
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0: # 데이터가 들어가 있다.
        for index in range(len(hash_table[hash_address])):
                if hash_table[hash_address][index][0] == index_key:
                    hash_table[hash_address][index][1] = value
                    return
        hash_table[hash_address].append([index_key,value])
    else: # 데이터가 없다.
        hash_table[hash_address] = [[index_key,value]] # 이 전체가 하나의 리스트

    

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(get_key(data))
    if hash_table[hash_address] !=0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None

save_data('Dd','1201023010')
save_data('Data','121131213313')

read_data('Dd')
print(hash_table)