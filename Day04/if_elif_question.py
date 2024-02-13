# 연습문제 11
score = float(input("학점을 입력하세요> "))
if score >= 4.5:
    grade = "A+"
elif score >= 4.25:
    grade = "A"
elif score >= 4.0:
    grade = "A-"
elif score >= 3.75:
    grade = "B+"
elif score >= 3.5:
    grade = "B"
elif score >= 3.25:
    grade = "B-"
elif score >= 3.0:
    grade = "C+"
elif score >= 2.75:
    grade = "C"
elif score >= 2.5:
    grade = "C-"
else:
    grade = "F"
print(f"당신의 학점은 {score}이고 등급은 {grade}입니다.")

