#!/usr/bin/env python3
import sys #외부 cmd에서 파일을 읽을 수 있게 해준다.

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as filereader : #input_file을 열고 읽는다.
    with open(output_file, 'w', newline='') as filewriter : #output_file을 열고 쓴다.
        header = filereader.readline() # header에 읽은 파일의 첫번줄을 저장한다.
        header = header.strip() #header에 불필요한 문자를 제거한다.
        header_list = header.split(',') #header_list에 header의 쉼표(,)를 기준으로 list화 한다.
        print(header_list) #header_list를 출력한다.
        filewriter.write(','.join(map(str,header_list))+'\n') #header_list를 문자로 하여, 한줄로 붙인다.
        for row in filereader: #행을 for문으로 돌린다.
            row = row.strip() #row에 불필요한 문자를 제거한다.
            row_list = row.split(',') #row_list에 row를 쉼표(,)를 기준으로 list화 한다.
            print(row_list) #row_list를 출력한다.
            filewriter.write(','.join(map(str,row_list))+'\n') #row_list를 다 붙인다.
