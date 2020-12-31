#pip install selenium 설치
#pip install beautifulsoup4 설치
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

fp = open("C:/Users/조민서/Desktop/python-selenium.txt", 'r', encoding='utf-8') #맞춤법 검사 할 파일
text = fp.read()
fp.close()

# 500자 나누기, (공백이 있을경우 그 전까지)
ready_list = []
while (len(text)>500):
    temp_str = text[:500] 
    last_space = temp_str.rfind(' ') # 마지막 공백 찾기
    temp_str = text[0:last_space]
    ready_list.append(temp_str)
    text = text[last_space:] # 마지막 공백부터 가져오기
ready_list.append(text) #마지막 남은 글 넣기

chrome_exe = "C:/Users/조민서/Desktop\chromedriver_win32/chromedriver.exe"

dv = webdriver.Chrome(chrome_exe) #크롬 exe 실행
dv.get("http://www.naver.com") #네이버 열기

elem = dv.find_element_by_name("query") #네이버 입력창
elem.send_keys("맞춤법 검사기") #입력
elem.send_keys(Keys.RETURN) # 엔터

time.sleep(1)
textarea = dv.find_element_by_class_name("txt_gray") # 맞춤법 검사기 원문

new_str = ''
for ready in ready_list:
    textarea.send_keys(Keys.CONTROL, "a") #전체 선택해서 검색 => 지우는 동시에 입력
    textarea.send_keys(ready) #검사할 내용
    
    elem = dv.find_element_by_class_name("btn_check") # 검사 버튼
    elem.click() #클릭
    time.sleep(2)
    soup = BeautifulSoup(dv.page_source, 'html.parser')
    st = soup.select("p._result_text.stand_txt")[0].text
    new_str += st.replace('.  ', '.\n')

fp = open("result.txt", 'w', encoding='utf-8')
fp.write(new_str)
fp.close()

#참고 https://m.blog.naver.com/jsk6824/221763151860
