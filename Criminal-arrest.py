#!/usr/bin/env python
# coding: utf-8

# In[136]:


import csv

f = open("범죄의 검거단서_전처리.csv")
crime = csv.reader(f)

for i in crime:
    print(i)
    
f.close()


# ### 3) 2016 - 2020 5년간 강력범죄(흉악) 검거 건수 평균 구하기 ###

# In[4]:


# 필요한 라이브러리 import 
# csv : csv 파일을 읽어오기 위한 csv 라이브러리
# numpy : 배열 연산을 위한 numpy 라이브러리
# math : 소수점 결과를 내림하기 위한 math 라이브러리
import csv
import numpy as np
import math

# open() : 파일 열기 함수를 이용, csv 파일을 읽어온 후
# csv.reader() : 파일 객체의 csv 파일을 읽어 들이는 함수를 이용하여 읽는다.
f = open("범죄의 검거단서_전처리.csv")
crime = csv.reader(f)
# crime 데이터의 첫번째 줄은 title로 지정, next() 함수 : 행을 가져오고, 다음행으로 이동할 때 사용, "리스트"로 출력된다.
title = next(crime)
# 각 년도, 단서별로 나누어진 강력범죄 검거수 데이터를 하나로 합치기 위한 arrkill 리스트 정의
arrkill = []

# for문을 사용하여 crime 안에 있는
for i in crime:
    # index 0번째 데이터, 범죄별 항목이 '강력범죄(흉악)'일 경우,
    if(i[0] == '강력범죄(흉악)'):
        # 2016 ~ 2020년 (2번째 열~6번째 열)까지의 검거 수 데이터를
        for j in range(2,7):
            # 위에서 생성한 arrkill 리스트에 append()하여 넣어준다.
            arrkill.append(int(i[j]))
# 리스트에 담긴 흉악범죄 (2016년 ~ 2020년) 검거 수 데이터들의 모든 평균(mean)을 구해준 후, ceil을 이용하여 소수점 버리기. 
deadful_crime = math.ceil(np.mean(arrkill))

# 2016 - 2020 4년간 강력범죄(흉악) 검거 건수 평균 출력
print("2016년부터 2020년까지 연간 흉악범죄 검거 건수의 평균(건) : 약" , deadful_crime, "건")

# 파일닫기
f.close()


# ### 4 - 1) 각 년도별 사기 범죄 검거 수의 총합 구하기. ###

# In[3]:


# 필요한 라이브러리 import 
# csv : csv 파일을 읽어오기 위한 csv 라이브러리
# numpy : 배열 연산을 위한 numpy 라이브러리
import csv
import numpy as np

# open() : 파일 열기 함수를 이용, csv 파일을 읽어온 후
# csv.reader() : 파일 객체의 csv 파일을 읽어 들이는 함수를 이용하여 읽는다.
f = open("범죄의 검거단서_전처리.csv")
crime = csv.reader(f)
# crime 데이터의 첫번째 줄은 title로 지정, next() 함수 : 행을 가져오고, 다음행으로 이동할 때 사용, "리스트"로 출력된다.
title = next(crime)

# 각 년도별로 사기범죄 "검거 수"를 저장할 리스트 생성 (2016 ~ 2020)
trick2016 = []
trick2017 = []
trick2018 = []
trick2019 = []
trick2020 = []

# crime 데이터 안에
for i in crime:
    # index 0번째 데이터, 범죄별 항목이 '사기'일 경우,
    if(i[0] == '사기'):
        # 위에서 생성한 각 년도에 해당하는 리스트에 append()로 열을 기준으로 검거 수 데이터를 추가힌다.
        # 이때 sum 연산을 위해 값은 int형으로 받아온다.
        # 2번째 열 = 2016년, 3번째 열 = 2017년 ... 6번째 열 = 2020년
        trick2016.append(int(i[2]))
        trick2017.append(int(i[3]))
        trick2018.append(int(i[4]))
        trick2019.append(int(i[5]))
        trick2020.append(int(i[6]))
         
# 제목, 텍스트 출력 '\t'으로 구분
print("\t\t 각 년도별 사기 범죄자 검거 수(총합)\t\t")
print()
print("2016년 \t 2017년 \t 2018년 \t 2019년 \t 2020년")

# 위의 리스트에 저장한 값들을 numpy 라이브러리의 sum()함수를 이용하여,
# 각 년도별 리스트 안의 검거 수값들의 총합을 구한다.
print(np.sum(trick2016),"\t",np.sum(trick2017),"\t",np.sum(trick2018),"\t",np.sum(trick2019),"\t",np.sum(trick2020))

print(trick2016)
print(trick2017)
print(trick2018)
print(trick2019)
print(trick2020)


# ### 4 - 2) 2016년부터 2020년까지 5년간 자수를 가장 많이 / 적게 한 범죄는? ###

# In[6]:


# 필요한 라이브러리 import 
# csv : csv 파일을 읽어오기 위한 csv 라이브러리
# numpy : 배열 연산을 위한 numpy 라이브러리
import csv
import numpy as np

# open() : 파일 열기 함수를 이용, csv 파일을 읽어온 후
# csv.reader() : 파일 객체의 csv 파일을 읽어 들이는 함수를 이용하여 읽는다.
f = open("범죄의 검거단서_전처리.csv")
crime = csv.reader(f)


# list1 : "자수"로 검거한 범죄와 단서 정보를 저장하기 위한 리스트 
# find_max : 총 자수 횟수의 최대값을 찾기 위한 리스트
# find_min : 총 자수 횟수의 최소값을 찾기 위한 리스트
list1 = []
find_max = []
find_min = []

# 해당 데이터는 총 22개의 단서로 분류하고 있는데, 범죄 유형 첫번째는 범죄 유형이 아닌, "합계"이다.
# 이러한 합계 행은 최소/최대를 구하는 데에 방해가 될 수 있기 때문에 제외한다.
# next() 함수 : 행을 가져오고, 다음행으로 이동할 때 사용, "리스트"로 출력된다.
for t in range(22):
    next(crime)

    # crime 함수 안에
for i in crime:
    # 검거 단서가 자수일 경우
    if i[1] == '자수':
        # total : 2016년~2020년까지의 각 범죄별 "자수" 횟수의 합을 구하기 위한 변수, 0으로 초기화
        # if문에 해당하는 행의 2번째 ~ 6번째열 (2016년 ~ 2020년)에 해당하는 검거 수의 총 합을 구한다.
        total = 0
        for j in range(2,7):
            total+= int(i[j])
            
        # 위에서 계산한 총 합과 해당 행의 범죄(0번째 열), 검거단서(1번째 열)의 정보도 list1에 함께 저장한다.
        list1 .append(i[0])
        list1 .append(i[1])
        list1 .append(total)


# list1에는 자수에 해당하는 범죄, 단서, 5년간의 총합에 대한 3가지 유형의 데이터가 22번 들어있다.
# 해당 데이터를 범죄,단서,5년간의 총합 "3개씩" 분리하기 위해 차원을 재구성해주는 reshape() 함수를 사용했다.
# 먼저 리스트 형태의 list1을 np.array()를 사용하여 배열 형태로 만든 다음, 
# 행의 개수 = 전체데이터길이/3, 열의 개수 = 3개로 2차원 배열로 재구성하여 array 변수에 할당한다.
array = np.array(list1).reshape(int(len(list1)/3),3)

# 재구성한 2차원 배열에서 2번째 열(검거 수) 데이터를 각각의 최댓값/최솟값을 구하는 리스트에 추가한다.
for i in range(len(array)):
    find_max.append(int(array[i][2]))
    find_min.append(int(array[i][2]))

# 최대값을 구하는 리스트를 이용, 검거수의 최대값을 구하는 과정
maxValue = find_max[0]
for i in range(1, len(find_max)):
    if maxValue < find_max[i]:
        maxValue = find_max[i]

# 최소값을 구하는 리스트를 이용, 검거수의 최소값을 구하는 과정
minValue = find_min[0]
for i in range(1, len(find_min)):
    if minValue > find_min[i]:
        minValue = find_min[i]    

# array 2차원 배열에서 
# 검거 수(2번째 열)이 최대값과 일치할 경우 해당 열의 범죄유형(0번째 열)과 총 건수 출력
print("'자수'를 가장 많이 한 범죄 유형 :", maxValue, "건")    
for i in range(0,len(array)):        
    if array[i][2] == str(maxValue):
        print(array[i][0])

        
# 중간 공백으로 띄어쓰기
print("")     

# array 2차원 배열에서 
# 검거 수(2번째 열)이 최소값과 일치할 경우 해당 열의 범죄유형(0번째 열)과 총 건수 출력
print("'자수'를 가장 적게 한 범죄 유형 :", minValue, "건")
for i in range(0,len(array)):
    if array[i][2] == str(minValue):
        print(array[i][0])


# ### 4 - 3) 가장 많은 저작권법위반을 검거한 단서 ###

# In[10]:


# 필요한 라이브러리 import 
# csv : csv 파일을 읽어오기 위한 csv 라이브러리
# numpy : 배열 연산을 위한 numpy 라이브러리
import csv
import numpy as np

# open() : 파일 열기 함수를 이용, csv 파일을 읽어온 후
# csv.reader() : 파일 객체의 csv 파일을 읽어 들이는 함수를 이용하여 읽는다.
f = open("범죄의 검거단서_전처리.csv")
crime = csv.reader(f)

# list1 : 저작권법 위반 범죄에 해당하는 행의 정보 (단서, 검거수)를 저장하기 위한 리스트
# find_max : 최대값을 찾기 위한 리스트
list1 = []
find_max = []

# crime 데이터 안에
for i in crime:
    # 범죄명(0번째 열)이 '저작권법' 위반이라면,
    if i[0] == '저작권법':
        # total : 2016년~2020년까지의 각 범죄별 "저작권법" 위반 횟수의 합을 구하기 위한 변수, 0으로 초기화
        # 해당 행에 있는 2016년(2번째 열)~2020년(6번째 열)의 검거수를 모두 더한다.
        # 이때 열 값은 연산을 위해 int형으로 받아온다.
        total = 0
        for j in range(2,7):
            total+= int(i[j])
        # list1 리스트에 '저작권법'에 해당하는 (범죄단서)과 (5년간의 검거수 총합)을 추가한다.
        list1.append(i[1])
        list1.append(total)

# 출력 데이터가 들어있는 list1데이터에
for k in range(1, len(list1)):
    #  index 값이 홀수 (= 5년간의 검거수 총합)인 데이터들을
    if k % 2 == 1:
        # 최대값을 찾아주는 리스트에 추가한다.
        # 최대값을 찾아주는 리스트에 추가된 5년간의 검거수 총합 데이터들 중 가장 큰 값 maxValue변수에 넣는다.
        find_max.append(list1[k])
        
        maxValue = np.max(find_max)
# 출력 데이터가 들어있는 list1데이터에       
for k in range(1, len(list1)):
    # index 값이 홀수 (= 5년간의 검거수 총합)인 데이터들 중
    if k % 2 == 1:
        # maxValue값과 같은 값은
        if list1[k] == maxValue:
            # 가장 많은 저작권법 위반을 검거한 단서이다.
            print("가장 많은 저작권법 위반을 검거한 검거 단서는")
            print(list1[k-1],"->", maxValue, "건")     


# ### 6) 직선 그래프 출력 : 2016-2020 성폭력 범죄 검거단서별 검거수 ###

# In[12]:


# 필요한 라이브러리 import 
# csv : csv 파일을 읽어오기 위한 csv 라이브러리
# numpy : 배열 연산을 위한 numpy 라이브러리
# matplotlib : 그래프를 그리기 위해 필요한 라이브러리
get_ipython().run_line_magic('matplotlib', 'inline')
import csv
import numpy as np
import matplotlib.pyplot as plt

# open() : 파일 열기 함수를 이용, csv 파일을 읽어온 후
# csv.reader() : 파일 객체의 csv 파일을 읽어 들이는 함수를 이용하여 읽는다.
f = open("범죄의 검거단서_전처리.csv")
crime = csv.reader(f)

# crime 데이터의 첫번째 줄은 title로 지정, next() 함수 : 행을 가져오고, 다음행으로 이동할 때 사용, "리스트"로 출력된다.
title = next(crime)

# 각 년도별로 성폭행죄 "검거 수"를 저장할 리스트 생성 (2016 ~ 2020)
array2016 = []
array2017 = []
array2018 = []
array2019 = []
array2020 = []

# clue : 22개의 검거 단서를 저장할 리스트
clue = [] 

# 읽어 온 crime 데이터 안에
for i in crime:
    # 범죄 유형이 성폭행인 행의
    if(i[0] == '성폭력'):
        # 2016~2020년의 검거수를 각 년도에 해당하는 리스트에 추가
        array2016.append(int(i[2]))
        array2017.append(int(i[3]))
        array2018.append(int(i[4]))
        array2019.append(int(i[5]))
        array2020.append(int(i[6]))
        
        # clue리스트에 22개의 검거단서 데이터 저장
        clue.append(i[1])
        
# 한글 글자깨짐 방지
plt.rcParams['font.family'] = 'NanumGothic'

# x 값은 각 검거단서 별 검거수, y값은 22개의 검거 단서 출력
# label : 범례표시
plt.plot(array2016, clue, label = "2016")
plt.plot(array2017, clue, label = "2017")
plt.plot(array2018, clue, label = "2018")
plt.plot(array2019, clue, label = "2019")
plt.plot(array2020, clue, label = "2020")

# x축 이름, y축 이름 생성
plt.xlabel('검거수')
plt.ylabel('검거단서')

# 오른쪽 상단에 범례 출력
plt.legend(loc="upper right")

# 그래프 제목 출력
plt.title("2016-2020 성폭력 검거단서별 검거수")

# 파일 닫기
f.close()


# In[ ]:




