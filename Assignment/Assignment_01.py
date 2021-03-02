#!/usr/bin/env python3
# 1번 문제
a = 2
b = 3
print("1) 정수 \na + b = {0}\n".format(a, b, a+b))
# 2번 문제
x = 8.5
y = 2.4
print("2) 실수 \nx / y = {0:.3f}\n".format(x/y))
# 3번 문제
str1 = "Is this the real life?"
str2 = "Is this just fantasy?"
print("3-1) 두 문자열을 더하시오.\n {0:s}".format(str1+str2))
# len함수는 공백 문자나 마침표 등을 포함하여 문자열 길이를 센다.
print("3-2) 더한 문자열의 길이를 구하시오.\n길이 : {0}\n".format(len(str1+str2)))

# 4번 문제
log = "[Wed Oct 11 14:32:52 2000] [error] [client 127.0.0.1] client denied by server configuration: /export/home/live/ap/htdocs/test"
str_list = log.split("] ",1)
print("4)split\nPiece1 : {0:s}\nPiece2 : {1:s}\n".format(str_list[0],str_list[1]))

# 5번 문제
str1_list = str1.split()
str2_list = str2.split()
print("5) 위 3)번의 두 문자열을 더해서 출력을 다음과 같이 하시오."
      "\nIs,this,the,real,life?,Is,this,just,fantasy?"
      "\n출력 : {0:s} \n".format(','.join(str1_list+str2_list)))

# 6번 문제
str3 = " Mamma mia, here I go again \t\t  \n"
str4 = "$$Mamma mia, does it show again.__--**"
str3_strip = str3.strip()
str4_strip = str4.strip('$_-*')
print("6-1)위 문자열 Str3에서 왼쪽 공백, 탭과 개행문자를 제거하시오.\n"
      "출력 : {0:s}\n"
      "6-2)위 문자열 Str4에서 $$, __, --, **를 제거하시오.\n"
      "출력 : {1:s}\n".format(str3_strip,str4_strip))






