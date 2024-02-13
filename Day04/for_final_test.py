# Final test
list_position = ['c.과장', 'b.부장', 'd.대리', 'a.사장', 'd.대리', 'c.과장']
non_overlap = [] # 중복되지 않은 직급
personnel = {} # 각 직급별 인원수

# 1
for position in list_position: # list position 중복 제거 후 추가
    if position not in non_overlap:
        non_overlap.append(position) 

# non_overlap2 = sorted(non_overlap) # non_overlap 정렬 # sorted는 내장함수, 값이 변하지 X
non_overlap.sort() # non_overlap 정렬 # sort()는 list 함수, 값 변경 가능


# print("중복되지 않은 직급 : ", non_overlap2)
print("중복되지 않은 직급 : ", non_overlap)

# 2
for position in list_position: # list position 값 = key, 숫자 = value
    if position in personnel:
        personnel[position] += 1
    else:
        personnel[position] = 1

sorted_personnel = dict(sorted(personnel.items())) # personnel 정렬
print("각 직급별 인원수 : ", sorted_personnel)

# 1 
lToS = set(list_position) # set(집합) 타입으로 형변환 + 중복제거
sToL = list(lToS) # list 타입으로 형변환
sToL.sort() # sToL 정렬
print(sToL) # ['a.사장', 'b.부장', 'c.과장', 'd.대리']

# 2
result_dict = {}
for x in sToL: # ['a.사장', 'b.부장', 'c.과장', 'd.대리']
    count = 0
    for y in list_position:
        if x == y:
            count += 1
    result_dict[x] = count # result_dict[x] (value)에 count (key)값 누적
print(result_dict)