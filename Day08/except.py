run = True
while run:
    try:
        num01 = int(input("분자 입력 : "))
        num02 = int(input("분모 입력 : "))
        print("결과 : ", num01/num02)
    except ValueError as ve:
        print(f"[{ve}]: 숫자를 입력해주세요")
    except ZeroDivisionError as zde:
        print(f"[{zde}]: 분모에 0이 아닌 정수를 입력해 주세요.")
    else:
        print("정상 수행되었습니다. 에러x")
        break
    finally:
        print("에러 유무와 관계없이 수행됩니다.")