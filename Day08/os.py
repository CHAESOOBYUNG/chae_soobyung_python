import os

# 현재 작업중인 디렉토리 경로 보여주는 명령어
print(os.getcwd())

# 현재 경로를 원하는 경로로 바꾸는 명령어
os.chdir("D:\chae_soobyung_python\Day08")
print(os.getcwd())

# 현재 디렉토리 내부의 구조를 보기위한 명령어
print(os.listdir())
for x in os.listdir():
    print(x)

# 현재 경로에 하나의 디렉토리 생성
# os.mkdir("sample")
# os.mkdir("sample/sample1")

# 현재 경로에 하나의 디렉토리 삭제
# os.rmdir("sample\sample1")
# os.rmdir("sample")
    
# 현재 경로에 여러개 디렉토리 생성
# os.makedirs("sample/sample1/sample2")

# 현재 경로에 여러개 디렉토리 삭제(내부에 타 파일 존재 X)
# os.removedirs("sample/sample1/sample2")

# 현재 경로에 여러개 디렉토리 삭제(내부에 타 파일 존재 X, 권장X)
# import shutil
# shutil.rmtree("sample/sample1/sample2")
    
# os.mkdir("sample")
os.chdir("D:\chae_soobyung_python\Day08\sample")

# 파일 만들기(open - 내장함수)
# open("파일명", "mode") # mode - w, r, s
# 순서 1) open
# 순서 2) write
# 순서 3) close
file = open("apple.txt", "w")
file.write("처음으로 입력하는 내용입니다.")
file.close()

file = open("apple.txt", "a")
file.write("두번째로 입력하는 내용입니다.")
file.close()

file = open("apple.txt", "r")
# print(file.read(5))
print(file.readline())
file.close()

# 삭제
# os.remove("D:\\chae_soobyung_python\\Day08\\sample\\apple.txt")