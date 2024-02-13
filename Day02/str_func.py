a = "python"
# count
print(a.count("o"))
print(a.count("z"))

# 문자열의 위치 파악(index, find)
word= "python"
print(word.find("p"))
print(word.find("o"))
print(word.find("z"))

print(word.index("o"))
# print(word.index("z"))

msg = "mega"
# 대문자 변환
print(msg.upper())
print(msg)

# 소문자 변환
msg = "MEGA"
print(msg.lower())

# 공백 제거
msg = "  yes"
print(msg.strip())
print(msg.strip().upper())

# 문자열 교체
msg = "I like baseball"
msg_replace = msg.replace("baseball", "football")
print(msg_replace)

# 예제 1
x = 2
Y = 2.5 * (x ** 2) + 3.3 * x + 6
print(f"2차 방정식 결과 = {Y}")

# 입력 함수 - input() -> 문자열 입력 받음
user_num = int(input("원하는 숫자를 입력하세요: ")) # 형변환
print(type(user_num), user_num * 10)

# 예제 2
word1 = input("첫번째 단어: ").upper()
word2 = input("두번째 단어: ").upper()
word3 = input("세번째 단어: ").upper()
abbr = word1[0] + word2[0] + word3[0]

print(f"첫번째 단어: {word1}")
print(f"두번째 단어: {word2}")
print(f"세번째 단어: {word3}")
print("="*10)

print(f"약자: {abbr}")