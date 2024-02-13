# 2개의 수를 받아 그 합을 돌려주는 함수
# def plus(x,y):
#     return x + y

plus = lambda x,y : x+y # lambda 함수
print(plus(1,2))

list_calFunc = [lambda x,y : x+y, lambda x,y : x-y]
print(list_calFunc[0](1,2))
print(list_calFunc[1](1,2))