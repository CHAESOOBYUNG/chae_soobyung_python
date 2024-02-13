# 학원의 정보(dict)
dict_profile = {
        "name": "mega",
        "address":"gangnam",
        "floor": 4
}
print(type(dict_profile), dict_profile)

# 값 조회
print(dict_profile["name"])

# 값 추가
dict_profile["phoneNum"] = "01011112222"
print(dict_profile)

# 값 수정
dict_profile["name"] = "MEGASTUDY"
print(dict_profile)

# 값 삭제 1
del dict_profile["floor"]
print(dict_profile)

# 값 삭제 2
print(dict_profile.pop("phoneNum"))
print(dict_profile)

# 모두 삭제
dict_profile.clear()
print(dict_profile)

# 확장
d1 = {"a": 1, "b": 2}
d2 = {"a": 2, "c": 3}
# d1.update(d2)
# print(d1)
d2.update(d1)
print(d2)

# 값 조회2 (get 함수)
print(d1.get("b"))
print(d1.get("c", "조회할 수 없는 key 값입니다."))

print(d1.keys())
print(d1.values())
print(d1.items())

result = list(d1.keys())
# result_list = list(result)
print(type(result), result)