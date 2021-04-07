from selenium import webdriver
import time
import sys

options = webdriver.ChromeOptions()

options.add_argument("start-maximized");
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

if  getattr(sys, 'frozen', False): 
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path, chrome_options = options)
else:
    driver = webdriver.Chrome(chrome_options = options)


#해당 url로 이동
url = "https://www.classcard.net/Login"
driver.get(url)
driver.implicitly_wait(5)

#아이디
id_input_xpath = '//*[@id="login_id"]'
driver.find_element_by_xpath(id_input_xpath).send_keys('아이디')
driver.implicitly_wait(5)

#비밀번호
password_input_xpath = '//*[@id="login_pwd"]'
driver.find_element_by_xpath(password_input_xpath).send_keys('비밀번호')
driver.implicitly_wait(5)

#로그인 버튼
login_btn_xpath = '//*[@id="loginForm"]/div[2]/button'
driver.find_element_by_xpath(login_btn_xpath).click()
driver.implicitly_wait(5)

#세트 클릭
level1_btn_xpath = '/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div/a'
driver.find_element_by_xpath(level1_btn_xpath).click()
driver.implicitly_wait(5)

#매칭 버튼 클릭
btn_box_study_xpath = '/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div[3]'
driver.find_element_by_xpath(btn_box_study_xpath).click()
driver.implicitly_wait(5)

#매칭 시작 버튼 클릭
start_btn_xpath = '//*[@id="newRankModal"]/div[2]/div/div/div[1]/div[4]/a[1]'
driver.find_element_by_xpath(start_btn_xpath).click()
driver.implicitly_wait(5)

def match():
    
    while 1:

        try:

            delay = 1.3
            time.sleep(delay)

            left_card_0_xpath = '//*[@id="left_card_0"]'
            left_card_1_xpath = '//*[@id="left_card_1"]'
            left_card_2_xpath = '//*[@id="left_card_2"]'
            left_card_3_xpath = '//*[@id="left_card_3"]'

            left_card_0 = driver.find_element_by_xpath(left_card_0_xpath)
            left_card_1 = driver.find_element_by_xpath(left_card_1_xpath)
            left_card_2 = driver.find_element_by_xpath(left_card_2_xpath)
            left_card_3 = driver.find_element_by_xpath(left_card_3_xpath)

            left_card_0_text_xpath = '//*[@id="left_card_0"]/div/div[2]/div/div[1]/span'
            left_card_1_text_xpath = '//*[@id="left_card_1"]/div/div[2]/div/div[1]/span'
            left_card_2_text_xpath = '//*[@id="left_card_2"]/div/div[2]/div/div[1]/span'
            left_card_3_text_xpath = '//*[@id="left_card_3"]/div/div[2]/div/div[1]/span'

            left_card_0_text = driver.find_element_by_xpath(left_card_0_text_xpath).text
            left_card_1_text = driver.find_element_by_xpath(left_card_1_text_xpath).text
            left_card_2_text = driver.find_element_by_xpath(left_card_2_text_xpath).text
            left_card_3_text = driver.find_element_by_xpath(left_card_3_text_xpath).text

            print(left_card_0_text)
            print(left_card_1_text)
            print(left_card_2_text)
            print(left_card_3_text)

            right_card_0_xpath = '//*[@id="right_card_0"]'
            right_card_1_xpath = '//*[@id="right_card_1"]'
            right_card_2_xpath = '//*[@id="right_card_2"]'
            right_card_3_xpath = '//*[@id="right_card_3"]'

            right_card_0 = driver.find_element_by_xpath(right_card_0_xpath)
            right_card_1 = driver.find_element_by_xpath(right_card_1_xpath)
            right_card_2 = driver.find_element_by_xpath(right_card_2_xpath)
            right_card_3 = driver.find_element_by_xpath(right_card_3_xpath)

            right_card_0_text_xpath = '//*[@id="right_card_0"]/div/div/div/div'
            right_card_1_text_xpath = '//*[@id="right_card_1"]/div/div/div/div'
            right_card_2_text_xpath = '//*[@id="right_card_2"]/div/div/div/div'
            right_card_3_text_xpath = '//*[@id="right_card_3"]/div/div/div/div'

            right_card_0_text = driver.find_element_by_xpath(right_card_0_text_xpath).text
            right_card_1_text = driver.find_element_by_xpath(right_card_1_text_xpath).text
            right_card_2_text = driver.find_element_by_xpath(right_card_2_text_xpath).text
            right_card_3_text = driver.find_element_by_xpath(right_card_3_text_xpath).text

            print(right_card_0_text)
            print(right_card_1_text)
            print(right_card_2_text)
            print(right_card_3_text)

            if left_card_0_text == right_card_0_text:
                left_card_0.click()
                right_card_0.click()
                continue

            elif left_card_0_text == right_card_1_text:
                left_card_0.click()
                right_card_1.click()
                continue

            elif left_card_0_text == right_card_2_text:
                left_card_0.click()
                right_card_2.click()
                continue

            elif left_card_0_text == right_card_3_text:
                left_card_0.click()
                right_card_3.click()
                continue

            elif left_card_1_text == right_card_0_text:
                left_card_1.click()
                right_card_0.click()
                continue

            elif left_card_1_text == right_card_1_text:
                left_card_1.click()
                right_card_1.click()
                continue

            elif left_card_1_text == right_card_2_text:
                left_card_1.click()
                right_card_2.click()
                continue

            elif left_card_1_text == right_card_3_text:
                left_card_1.click()
                right_card_3.click()
                continue

            elif left_card_2_text == right_card_0_text:
                left_card_2.click()
                right_card_0.click()
                continue

            elif left_card_2_text == right_card_1_text:
                left_card_2.click()
                right_card_1.click()
                continue

            elif left_card_2_text == right_card_2_text:
                left_card_2.click()
                right_card_2.click()
                continue

            elif left_card_2_text == right_card_3_text:
                left_card_2.click()
                right_card_3.click()
                continue

            elif left_card_3_text == right_card_0_text:
                left_card_3.click()
                right_card_0.click()
                continue
                
            elif left_card_3_text == right_card_1_text:
                left_card_3.click()
                right_card_1.click()
                continue

            elif left_card_3_text == right_card_2_text:
                left_card_3.click()
                right_card_2.click()
                continue

            elif left_card_3_text == right_card_3_text:
                left_card_3.click()
                right_card_3.click()
                continue

        except:
            continue


match()

