hash_table = list(0 for i in range(10))

# 제일 간단한 해쉬함수
def hash_func(key):
    return key % 5 # 나머지 연산

# 해쉬 테이블에 저장해보기
data1= 'Andy'
data2 = 'Dave'
data3 = 'Trump'

## ord() : 문자의 ASCII 코드 리턴
print(ord(data1[0]),ord(data2[0]),ord(data3[0])) #문자 맨 앞글자를 key값 활용

print(hash_func(ord(data1[0]))) # 이게 해쉬 주소

# 해쉬 테이블에 값 저장 예
def storage_data(data,value):
    key= ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value


# 해쉬 테이블에서 특정 주소의 데이터 값 가져오기
storage_data('Andy','01055553333')
storage_data('Dave','01044443333')
storage_data('Trump','01022223333')

#데이터를 저장하고 읽어보기
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy'))