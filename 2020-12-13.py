# # 63강. 모듈
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) #4명이서 조조 할인 영화 보러 갔을때
# theater_module.price_soldier(5) #5명이 군인이 영화 보러갔을 때

# import theater_module as mv
# mv.price(3)
# mv.price_moring(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_moring(4)
# price_soldier(5)

# from theater_module import price, price_moring
# price(5)
# price_moring(6)
# # price_soldier(4)

# from theater_module import price_soldier as price
# price(3)


# 64강. 패키지
# 모듈들을 모아놓은 집합
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to = detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# # 65강. __all__
# # from random import *
# from travel import *
# # # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# # 66강 모듈 직접 실행
# from travel import *
# # # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# 67강. 패키지, 모듈 위치
# import inspect
# import random
# from travel import *
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# # 68강. pip install
# # https://pypi.org/search/
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 69강 내장함수
# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# 구글에서 list of python builtins
# https://docs.python.org/3/library/functions.html

# 70강. 외장함수
# 구글에서 list of python modules
# https://docs.python.org/3/py-modindex.html
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os 
# print(os.getcwd()) # 현재 디렉토리


# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")

# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()
# td = datetime.timedelta(days=100) # 100일 저장
# print("우리가 만난지 100일은", today+td)

# 71강. 퀴즈 10
'''
Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

조건 : 모듈 파일명은 byme.py로 작성

(모듈 사용 예제)
import byme
byme.sign()

(출력 예제)
이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : xxx
이메일 : xxx. 
'''
import byme
byme.sign()