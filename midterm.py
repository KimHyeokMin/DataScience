
# coding: utf-8

# In[1]:

#문제1: 문자열 속 숫자들의 합 구하기


# In[2]:

def sum_str(x):
    #split 함수를 이용하여 구분자로 데이터를 자른다.
    #list(map()) 을 이용하여 전체에 대해 int(숫자형)형으로 변경한다.
    #sum 함수를 이용하여 전체 합산
    result = sum(list(map(int,x.split(','))))
    return result


# In[3]:

#문제2: 설날까지 남은 시간 


# In[12]:

def until_new_year():
    import arrow
    #한국 시간 기준으로 설날에서 현재시간을 차감.
    result = arrow.get('2017-01-30 00:00').replace(tzinfo='Asia/Seoul') - arrow.now().to('Asia/Seoul')
    #결과를 day 타입으로 변경하여 리턴
    return result.days


# In[5]:

#문제3: UserAgentString 분석


# In[6]:

def ua_string(x):
    if 'Chrome' in x:
        return('C')
    elif 'Safari' in x:
        return('S')
    elif 'Firefox' in x:
        return('F')
    else:
        return('I')


# In[7]:

#문제4: 결측값 제거


# In[8]:

def del_nan_row(x):
    dropna_x=x.dropna(how='all')
    return(dropna_x)

