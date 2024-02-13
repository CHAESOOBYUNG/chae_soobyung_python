# 1
num = 100
if num > 10:
    print("True")
elif num > 30:
    print("True")
elif num > 50:
    print("True")
else:
    print("True")

# 2
money = input("가지고 있는 돈> ")
if money >= 10000:
    print("택시")
elif 2000 <= money:
    print("킥보드")
elif 1000 <= money:
    print("버스")
else:
    print("걷는다")

# 3
score = 92
# if score >= 90:
#     print("합격")
# else:
#     print("불합격")
print("합격") if score >= 90 else print("불합격")

# if score >= 90:
#     result = "합격"
# else:
#     result = "불합격"
result = "합격" if score >= 90 else "불합격"
print(result)