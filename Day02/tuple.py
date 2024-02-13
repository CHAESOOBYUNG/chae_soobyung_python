# 튜플 - 수정, 삭제 X
t1 = (1,2,3, "사")
print(type(t1), t1)

# 조회 가능
print(t1[0])
print(t1[3])

# 수정 불가
# t1[3] = "오" 

# 삭제 불가
# del t1[3]
# t1.remove(10)

t1 = (10, 20, 30, 40, 50)
print(len(t1))

# 결과가 튜플인 함수
print(divmod(10, 3))
print(divmod(10, 3)[0]) # 몫
print(divmod(10, 3)[1]) # 나머지
