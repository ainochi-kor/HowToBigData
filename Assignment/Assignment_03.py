#!/usr/bin/env python3
'''
1.4.6 튜플
튜플은 변경할 수 없다.
const처럼.
'''

#23) 튜플 생성하기
her_tuple = ('a','b','c','d')
his_tuple = ('e','f','g')

sum_tuple = her_tuple + his_tuple
print("23) 위 두 튜플을 병합하고 병합한 튜플의 원소의 개수를 구하시오.")
print("병합한 튜플 : {}".format(sum_tuple))
print("튜플의 원소 갯수 : {}\n".format(len(sum_tuple)))

#24) 튜플 풀기
print("24) 위 her_tuple의 원소들을 변수 A, B, C, D에 풀어 내시오.")
A, B, C, D = her_tuple
print("풀어진 튜플 : {}, {}, {}, {}\n".format(A,B,C,D))

#25) 튜플을 리스트로 변환하기
my_list = [1, 2, 3]
my_tuple = ('x','y','z')
print("25) 예제를 테스트 해 보시오. ")
print("tuple화 : {}".format(tuple(my_list)))
print("list화 : {}\n".format(list(my_tuple)))

'''
1.4.7 딕셔너리
'''

#26) 딕셔너리 생성하기
my_dict = {'python' : 1, 'bigdata' : 2, 'analysis' : 3}
print("26) 딕셔너리의 길이를 구하시오.")
print("딕셔너리의 길이 : {}\n".format(len(my_dict)))

#27) 딕셔너리 내 값 접근하기
print("27) 키 ‘bigdata’의 값을 출력하시오.")
print(" bigdata 키의 값 : {}\n".format(my_dict['bigdata']))

#28) 복사하기
print("28) 26번의 my_dict을 his_dict에 복사하시오.")
his_dict = my_dict.copy()
print("his_dict : {}\n".format(his_dict))

#29) 키, 값, 아이템
print("29) my_dict 의 키, 값, 아이템을 출력하시오.")
print("my_dict.keys() : {}".format(my_dict.keys()))
print("my_dict.values() : {}".format(my_dict.values()))
print("my_dict.items() : {}\n".format(my_dict.items()))

#30) in, not in, get 이용하기
print("30) 예제를 테스트하시오.")
a_dict = {'one': 1, 'two': 2, 'three': 3}
another_dict = {'x': 'printer', 'y': 5, 'z': ['star', 'circle', '9']}
if 'y' in another_dict:
    print("y is a key in another_dict : {}".format(another_dict.keys()))
if 'c' not in another_dict:
    print("c is a key in another_dict : {}".format(another_dict.keys()))
print("Output : {!s}".format(a_dict.get('three')))
print("Output : {!s}".format(a_dict.get('four')))
print("Output : {!s}\n".format(a_dict.get('four','Not in dict')))

#31) 정렬하기
print("31-1) my_dict의 사본을 your_dict으로 만드시오.")
your_dict = my_dict.copy()
print("your_dict : {}".format(your_dict))
your_dict = sorted(your_dict.items(), key=lambda item:item[0])
print("31-2) 키를 기준으로 오름차순으로 정렬하시오.")
print("오름차순 : {}".format(your_dict))

'''
1.4.8 제어 흐름
'''

#32) if-else
print


