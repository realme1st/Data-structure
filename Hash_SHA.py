# #SHA-1
import hashlib

# data = 'test'.encode() # 바이트로 바꿔준다.

# hash_object = hashlib.sha1()
# hash_object.update(data) 
# hex_dig = hash_object.hexdigest() #16진수로
# print(hex_dig) #해쉬값

# #SHA-256
# # 이 경우는 hashlib.sha256() 으로하면 되는데 더 보안이 좋음.

# 해쉬 함수 : key % 8
# 해쉬 키 생성 : hash(data)

hash_table = list([0 for i in range(8)])

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig,16) 

def hash_function(key):
    return key % 8

def save_data(data,value):
    index_key = get_key(data) # 별도로 key 저장
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0: # 데이터가 들어가 있다.
        for index in range(hash_address,len(hash_table)):
            if hash_table[index]==0:
                hash_table[index] =[index_key,value]
                return
            elif hash_table[index][0] ==index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key,value]
    

    

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] !=0:
        for index in range(hash_address,len(hash_table)):
            if hash_table[index] ==0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None

