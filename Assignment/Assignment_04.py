#!/usr/bin/env python3
import numpy as np
import pandas as pd
'''
1.4.9 함수
'''
def getMean(numbericValues):
    return sum(numbericValues)/len(numbericValues) if len(numbericValues) > 0 else float('nan')
your_list = [75, 80, 90, 95, 60, 72, 88, 92, 84, 72]
dataframe = pd.DataFrame(your_list)
print("Output function : {!s}".format(getMean(your_list)))
print("Output numpy.mean : {}".format(np.mean(your_list)))
print("Output pandas.mean : {}\n".format(dataframe.mean()))

'''
1.4.10 예외
- 85쪽, try-except
- 86쪽, try-except-else-finally을 테스트 해# 보세요.
'''
# 숫자 시퀀스의 평균 계산하기
def getMean(numericValues):
    return sum(numericValues)/len(numericValues)

my_list2 = [ ]

# 짧은 버전
try:
    print("Output : {}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
    print("Output (Error): {}".format(float('nan')))
    print("Output (Error): {}\n".format(detail))

# 긴 버전
try:
    result = getMean(my_list2)
except ZeroDivisionError as detail:
    print("Output (Error): {}".format(float('nan')))
    print("Output (Error): {}".format(detail))
else:
    print("Output (The mean is) : {}".format(result))
finally:
    print("Output (Finally) : The finally block is executed every time")
'''
1.5 텍스트 파일 읽기
※ 데이터 분석을 하려면 외부의 파일을 읽어 들입니다.
- 86쪽부터 91쪽까지 예제대로 테스트하기 바랍니다.
'''

#!/usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys

#파일 읽기
#하나의 텍스트 파일 읽기
print("Output : ")
#input_file = sys.argv[1]
input_file = "src/test01.txt"
filereader = open(input_file, 'r')
for row in filereader:
    print(row.strip())
filereader.close()

print("\nOutput : ")
with open(input_file, 'r', newline='') as filereader:
    for row in filereader:
        print("{}".format(row.strip()))

'''
1.6 glob을 이용해 다수의 텍스트 파일 읽기
※ 데이터 분석을 위해서 여러 파일을 읽어 들이는 일이 있습니다.
- 91쪽부터 95쪽까지 예제대로 테스트를 해 보세요.
'''

#!/usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
import glob
import os

#다수의 파일 읽기
print("Output : ")
#inputPath = sys.argv[1]
inputPath = "src"
for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
    with open(input_file, 'r', newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))


'''
1.7 텍스트 파일 쓰기
※ 데이터 분석에서 대부분의 출력 결과는 파일에 씁니다.
- 95쪽부터 99쪽까지 파일 쓰기 방법을 테스트 해 보세요.
'''

#파일 작성하기
#하나의 텍스트 파일 작성하기
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
max_index = len(my_letters)
#output_file = sys.argv[1]
output_file = "src/write_to_file.txt"
filewriter = open(output_file, 'w')
for index_value in range(len(my_letters)):
    if index_value < (max_index-1) :
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print("\nOutput : Output written to file")

# CSV 파일 작성하기
my_numbers = [0,1,2,3,4,5,6,7,8,9]
max_index = len(my_letters)
output_file = "src/write_to_file.txt"
filewriter = open(output_file, 'a')
for index_value in range(len(my_numbers)):
    if index_value < (max_index-1):
        filewriter.write(str(my_numbers[index_value])+',')
    else:
        filewriter.write(str(my_numbers[index_value])+'\n')
filewriter.close()
print("Output : Output appended to file")

