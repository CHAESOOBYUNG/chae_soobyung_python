# 숫자형 자료형을 이용한 사칙연산
num01 = 10
num02 = 20

# 덧셈
print("덧셈 결과: ", num01 + num02)
# 뺄셈
print("뺄셈 결과: ", 10 - 20)
# 곱셈
print("곱셈 결과: ", num01 * num02)
# 나눗셈
print("나눗셈 결과: ", num01 / num02)
# 몫 - //
print("몫 결과: ", num01 // num02)
# 나머지 - %
print("나머지 결과: ", num01 % num02)

# 육개장 1개의 가격을 선정 -> 계산
price = 12000
pocket = 50000
print("육개장 1개의 가격: ", price)
print("육개장 3개의 가격: ", price * 3)
print("보유 현금: ", pocket)
print("3개 산 후 거스름돈: ", pocket - 3 * price)

num_int = 1
num_float = 1.0
print(type(num_int))
print(type(num_float))

# 2진수
# bin() - 소괄호 내부의 수를 2진수로 변환하여 돌려주는 역할
print(bin(10))
# 8진수
# oct() - 소괄호 내부의 수를 8진수로 변환하여 돌려주는 역할
print(oct(10))
# 16진수
# hex() - 소괄호 내부의 수를 16진수로 변환하여 돌려주는 역할
print(hex(10))

print(0b1010)
print(0o12)
print(0xa)

# 제곱 - **
print(2**2)
print(pow(2, 4))