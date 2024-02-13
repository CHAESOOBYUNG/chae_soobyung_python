a = "20241225Christmas"
date = a[:8] # 20241225
day = a[8:]

# 문자열 포메팅
print("date는 day입니다.")

# 방법 1
print("%s는 %s입니다."%(date, day)) # 정수: %d, 소수: %f, %s: 문자열

# 방법 2
print("{}는 {}입니다.".format(date, day))

# 방법 3
print(f"{date}는 {day}입니다.")

# 예제
year = 2024
animal = "용"
print("올해는 %d년 %s의 해입니다."%(year, animal))
print("올해는 {}년 {}의 해입니다.".format(year, animal))
print(f"올해는 {year}년 {animal}의 해입니다.")