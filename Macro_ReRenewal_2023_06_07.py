from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

options = webdriver.ChromeOptions()

options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

if getattr(sys, "frozen", False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
else:
    driver = webdriver.Chrome(chrome_options=options)


# 해당 url로 이동
url = "https://www.classcard.net/Login"
driver.get(url)
driver.implicitly_wait(5)

# 아이디
id_input_xpath = '//*[@id="login_id"]'
driver.find_element_by_xpath(id_input_xpath).send_keys("아이디")
driver.implicitly_wait(5)

# 비밀번호
password_input_xpath = '//*[@id="login_pwd"]'
driver.find_element_by_xpath(password_input_xpath).send_keys("비밀번호")
driver.implicitly_wait(5)

# 로그인 버튼
login_btn_xpath = '//*[@id="loginForm"]/div[3]/button'
driver.find_element_by_xpath(login_btn_xpath).click()
driver.implicitly_wait(5)

# 세트 클릭
level1_btn_xpath = (
    "/html/body/div[1]/div[2]/div/div/div[2]/div[3]/div/div[3]/div[3]/div/a"
)
driver.find_element_by_xpath(level1_btn_xpath).click()

engWordElm = driver.find_elements(
    By.CSS_SELECTOR, ".flip-body > .flip-card > .ex_front.hidden"
)
korWordElm = driver.find_elements(
    By.CSS_SELECTOR, ".flip-body > .flip-card > .ex_back.hidden"
)

wordDict = {}

for i in range(len(engWordElm)):
    print(engWordElm[i].get_attribute("innerHTML"))
    wordDict[engWordElm[i].get_attribute("innerHTML")] = korWordElm[i].get_attribute(
        "innerHTML"
    )

print(len(engWordElm))

driver.implicitly_wait(5000)


# 매칭 버튼 클릭
btn_box_study_xpath = "/html/body/div[2]/div/div[2]/div[1]/div[5]"
driver.find_element_by_xpath(btn_box_study_xpath).click()
driver.implicitly_wait(5)

# 매칭 시작 버튼 클릭
start_btn_xpath = '//*[@id="wrapper-learn"]/div[1]/div[1]/div/div/div[2]/div[4]/a'
driver.find_element_by_xpath(start_btn_xpath).click()
driver.implicitly_wait(5)


def match():

    right_card_0_xpath = '//*[@id="right_card_0"]'
    right_card_1_xpath = '//*[@id="right_card_1"]'
    right_card_2_xpath = '//*[@id="right_card_2"]'
    right_card_3_xpath = '//*[@id="right_card_3"]'

    left_card_0_xpath = '//*[@id="left_card_0"]'
    left_card_1_xpath = '//*[@id="left_card_1"]'
    left_card_2_xpath = '//*[@id="left_card_2"]'
    left_card_3_xpath = '//*[@id="left_card_3"]'

    left_card_0_text_xpath = '//*[@id="left_card_0"]/div/div[1]/div/div'
    left_card_1_text_xpath = '//*[@id="left_card_1"]/div/div[1]/div/div'
    left_card_2_text_xpath = '//*[@id="left_card_2"]/div/div[1]/div/div'
    left_card_3_text_xpath = '//*[@id="left_card_3"]/div/div[1]/div/div'

    right_card_0_text_xpath = '//*[@id="right_card_0"]/div/div/div/div'
    right_card_1_text_xpath = '//*[@id="right_card_1"]/div/div/div/div'
    right_card_2_text_xpath = '//*[@id="right_card_2"]/div/div/div/div'
    right_card_3_text_xpath = '//*[@id="right_card_3"]/div/div/div/div'

    time.sleep(0.2)

    while 1:

        delay = 1.15
        time.sleep(delay)

        try:
            left_card_0 = driver.find_element_by_xpath(left_card_0_xpath)
        except:
            left_card_0 = None
            continue
        try:
            left_card_1 = driver.find_element_by_xpath(left_card_1_xpath)
        except:
            left_card_1 = None
            continue
        try:
            left_card_2 = driver.find_element_by_xpath(left_card_2_xpath)
        except:
            left_card_2 = None
            continue
        try:
            left_card_3 = driver.find_element_by_xpath(left_card_3_xpath)
        except:
            left_card_3 = None
            continue

        try:
            left_card_0_textEng = driver.find_element_by_xpath(
                left_card_0_text_xpath
            ).get_attribute("innerHTML")
        except:
            left_card_0_textEng = None
            continue
        try:
            left_card_1_textEng = driver.find_element_by_xpath(
                left_card_1_text_xpath
            ).get_attribute("innerHTML")
        except:
            left_card_1_textEng = None
            continue
        try:
            left_card_2_textEng = driver.find_element_by_xpath(
                left_card_2_text_xpath
            ).get_attribute("innerHTML")
        except:
            left_card_2_textEng = None
            continue
        try:
            left_card_3_textEng = driver.find_element_by_xpath(
                left_card_3_text_xpath
            ).get_attribute("innerHTML")
        except:
            left_card_3_textEng = None
            continue
        try:
            left_card_0_text = wordDict[left_card_0_textEng]
        except:
            left_card_0_text = None
            continue
        try:
            left_card_1_text = wordDict[left_card_1_textEng]
        except:
            left_card_1_text = None
            continue
        try:
            left_card_2_text = wordDict[left_card_2_textEng]
        except:
            left_card_2_text = None
            continue
        try:
            left_card_3_text = wordDict[left_card_3_textEng]
        except:
            left_card_3_text = None
            continue

        try:
            right_card_0 = driver.find_element_by_xpath(right_card_0_xpath)
            right_card_1 = driver.find_element_by_xpath(right_card_1_xpath)
            right_card_2 = driver.find_element_by_xpath(right_card_2_xpath)
            right_card_3 = driver.find_element_by_xpath(right_card_3_xpath)

            right_card_0_text = driver.find_element_by_xpath(
                right_card_0_text_xpath
            ).get_attribute("innerHTML")
            right_card_1_text = driver.find_element_by_xpath(
                right_card_1_text_xpath
            ).get_attribute("innerHTML")
            right_card_2_text = driver.find_element_by_xpath(
                right_card_2_text_xpath
            ).get_attribute("innerHTML")
            right_card_3_text = driver.find_element_by_xpath(
                right_card_3_text_xpath
            ).get_attribute("innerHTML")

            print("==============================")
            print(left_card_0_text, "|", right_card_0_text)
            print(left_card_1_text, "|", right_card_1_text)
            print(left_card_2_text, "|", right_card_2_text)
            print(left_card_3_text, "|", right_card_3_text)
            print("==============================")

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
