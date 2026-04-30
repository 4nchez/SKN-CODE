# path(파일 경로) 로 표현 : my_collections/test_list/list_sample.py
# 함수들만 저장되어 있는 소스 파일 == 모듈(module) 이라고 함
# 모듈들을 모아놓은 폴더 == 패키지(package) 라고 함
# 모듈로 표현 : my_collections.test_list.list_sample

# 리스트(list) 사용 테스트용 함수들 제공하는 스크립트

'''
파이썬 리스트(list) 자료형
파이썬이 제공하는 군집 자료형임 (자바의 List 와 같은 자료형임)

개념 : 여러 종류의 값들을 순차적으로 저장하는 자료형임
저장 용량에 제한이 없음
저장되는 값의 종류에도 제한이 없음
저장 순서에 대한 순번(인덱스, index)가 있음 => 인덱싱, 슬라이싱 연산 가능
'''

# 리스트 생성방법1 : list() 함수 사용
def make_list1():
    # print('make_list1() 함수 실행됨')
    lst = list()
    print(lst, type(lst), id(lst))
    
    return # 함수 코드 맨 마지막에 반드시 존재하며, 생략할 수 있음

# 리스트 생성방법2 : [] 대괄호 사용
def make_list2():
    lst = []
    print(lst, type(lst), id(lst))
    return

# list 자료형 특징 1: 문자열(str)과 같이 인덱싱, 슬라이싱 연산이 가능함
# index (순번: 저장 순서, 0부터 시작함)
# 인덱싱 표현 : 리스트변수[순번]
def list_indexing():
    lst = [1, 2, 3, 'python', 3.45, [11, 22, 33], True, False, None]
    print('0번째 기록된 값 조회 : ', lst[0])