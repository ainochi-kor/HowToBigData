#!/usr/bin/env python3
# 7번 문제
str5 = "Thunderbolts and lightning very very frightening me."
str5_replace = str5.replace(" ",", ")
print("7)위 문자열 사이의 공백을 쉼표(,)로 치환해서 아래와 같이 출력하시오. (CSV)\n"
      "출력 : {0:s}\n".format(str5_replace))

# 8번 문제
str6 = "imagine there's no heaven"
str6_capitalize = str6.capitalize()
print("8) 위 문자열의 첫 번째 문자를 대문자로 바꾸시오.\n"
      "출력 : {0:s}\n".format(str6_capitalize))

# 9번 문제
import re
str7 = "Na, na, na, na-na-na na Na-na-na na, hey Jude Na, na, na, na-na-na na Na-na-na na, hey Jude"
str7_list = str7.split()
pattern = re.compile(r"hey", re.I)
count = 0
for word in str7_list:
      if pattern.search(word):
            count += 1
print("9) 위 문자열에서 hey가 나타난 횟수를 출력하시오. \n"
      "횟수 : {0}\n".format(count))

# 10번 문제
print("10) 위 9)번의 문자열에서 Jude가 나타나면 출력하시오.")
pattern = re.compile(r"(?P<match_word>Jude)", re.I)
for word in str7_list:
      if pattern.search(word):
            print(pattern.search(word).group(('match_word')))

# 11번 문제
str7_to_find = r"Jude"
pattern = re.compile(str7_to_find, re.I)
print("\n11) 위 9)번의 문자열에서 Jude를 Zude로 바꾸시오.\n"
      "출력 : {0:s}\n".format(pattern.sub("Zude", str7)))

# 12번 문제
from datetime import date, time, datetime, timedelta
current_datetime = datetime.today()
print("12-1) 오늘의 datetime을 출력하시오. \n"
      "datetime : {!s}".format(current_datetime))
print("12-2) 오늘의 datatime이 2020-03-02 00:00:00 이라고 가정하자. \n"
      "오늘의 datetime을 입력해서 시, 분, 초는 버리고 연, 월, 일만 출력하시오.")
print("출력 : {!s}\n".format(current_datetime.strftime('%Y,%m/%d')))

# 13번 문제
print("13) 아래와 같이 두 리스트를 만드시오.")
x_list = [1,3,5,7,9]
y_list = [2,4,6,8,10]
print("x_list = {0} \n"
      "y_list = {1}".format(x_list,y_list))

# 14번 문제
x_list_len = len(x_list)
x_list_min = min(x_list)
x_list_max = max(x_list)
print("14) x_list에서 len, min, max, count를 구하시오.\n"
      "len : {}\nmin : {} \nmax : {}\n".format(x_list_len,x_list_min,x_list_max))

# 15번 문제
print("15) x_list의 마지막 원소를 인덱스를 이용하여 출력하시오. [-1] 사용.\n"
      "x_list의 마지막 원소 : {}\n".format(x_list[-1]))

# 16번 문제
print("16) x_list에서 2번째 원소부터 시작하여 뒤에 남은 모든 원소를 출력하시오.\n"
      "출력 : {}\n".format(x_list[1:]))

# 17번 문제
print("17) x_list와 y_listh를 병합하시오.\n"
      "출력 : {}\n".format(x_list+y_list))

# 18번 문제
print("18) x_list에 3 이 있으면 True 없으면 False를 출력하시오.\n"
      "출력 : {}\n".format(3 in x_list))

# 19번 문제
print("19) x_list에 11, 13, 15를 추가하고 y_list에 12, 14를 추가하시오.")
x_list.append(11); x_list.append(13); x_list.append(15)
y_list.append(12); y_list.append(14)
print("x_list = {}\ny_list = {}\n".format(x_list,y_list))

# 20번 문제
print("20) reverse 함수는 리스트 내용을 역순으로 변경합니다.")
x_list.reverse()
print("x_list = {}\n".format(x_list))

# 21번 문제
z_list = x_list+y_list
z_list.sort()
print("21) x_list와 y_list를 병합한 결과를 z_list라고 두고 z_list를 sort 하시오.\n"
      "z_list = {}\n".format(z_list))

# 22번 문제
from operator import itemgetter

your_list = [[99, 2, 2, 555], [99, 4, 4, 554], [456, 6, 6, 879], [234, 7, 7, 909]]
your_list_lamda = sorted(your_list, key=lambda index_value: index_value[2])
your_list_itegetter = sorted(your_list, key=itemgetter(0,3))
print("22-1) 인덱스 2에 위치한 값(즉 3번째 값)에 따라 정렬하시오. (lamda 함수)\n"
      "your_list_lamda = {}".format(your_list_lamda))
print("22-2) 인덱스 0에 위치한 값으로 먼저 정렬하고 3에 위치한 값으로 다음 정렬하시오. (itemgetter)\n"
      "your_list_itegetter = {}".format(your_list_itegetter))