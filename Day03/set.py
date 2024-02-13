s1 = {1,2,3,1,2}
print(type(s1), s1)

s2 = {"h", "e", "l", "l", "o"}
print(s2)

# 합집합
s1 = {1,2,3,4}
s2 = {3,4,5,6}
# 함수 사용
print(s1.union(s2))
# 기호 사용
print(s1 | s2)

# 교집합
print(s1.intersection(s2))
print(s1 & s2)

# 차집합
print(s1.difference(s2))
print(s1 - s2)
print(s2.difference(s1))
print(s2 - s1)

# 하나의 데이터 추가
s1.add(4)
print(s1)

# 여러개 데이터 추가
s1.update([5, 6, 7])
s1.update((5, 6, 7)) # 자동 형변환 -> 각각의 값 추가
print(s1)

# 삭제(remove, discard)
s1.remove(7)
print(s1)
s1.discard(7)
print(s1)

