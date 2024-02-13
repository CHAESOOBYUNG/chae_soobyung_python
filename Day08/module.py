import super

test = super.New(1000)
test.print_profile()

# sys 모듈(외장) import
import sys

# 파이썬 경로(path) 확인
print(sys.path)

# 파이썬 경로(path) 추가
sys.path.append("D:\\chae_soobyung_python\\Day07")
print(sys.path)

# 선언 방식에 따른 호출 1
import sample
print(sample.plus(10,20))

# 선언 방식에 따른 호출 1
from sample import plus
print(plus(10,20))

print(__name__)
