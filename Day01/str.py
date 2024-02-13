msg = "수업3시간째..."
print(msg)

num01 = "10"
print(type(num01), num01)

# 특정 문자 강조하기
word = "Hello Python"
word02 = "\"H\"ello \nPython"
word03 = 'Hello \'P\'ython'
word04 = '''
'P'ython'''
print(word)
print(word02)
print(word03)
print(word04)

# 문자열 합치기
word01 = "python"
word02 = "is fun"
print(word01 + word02) # 공백기능 X
print(word01, word02) # 공백기능 O

mark = "="
print(mark * 30)

# 인덱싱
msg02 = "Python is fun"
print(msg02)
print(msg02[10] + msg02[11] + msg02[12])

# 슬라이싱
print(msg02[10:13]) # 10 ~ 12번째 글자
print(msg02[10:]) # 10 ~ 끝 글자
print(msg02[:6]) # 처음(0) ~ 5번째 글자

alpa = "abcdefg"
print(alpa[::2]) # 2칸씩 띄어서 가져옴

# 예제
a = "20241225Christmas"
date = a[:8] # 20241225
day = a[8:]
print(f"{date}는 {day}입니다.")

for i in a:
    print(i)

