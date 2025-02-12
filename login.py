from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_main():
    # 如果你没有将ChromeDriver添加到系统PATH中，可以指定其路径
    # service = Service('path/to/chromedriver')
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome()
    try:
        # 打开登录页面
        driver.get('https://www.fenbi.com')

        wait = WebDriverWait(driver, 10)

        #登录按钮
        try:

            #找登录按钮
            login_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > app-root > div > div.fenbi-web-header > fb-header > div > div.info-wrapper > button'))
            )

            # 找到登录按钮，点击它
            login_button.click()
            # 等待登录页面加载
            time.sleep(3)

            # 查找并点击“账号密码登录”切换按钮
            account_password_login_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[1]/fb-header/div[2]/div/div[2]/div[5]/div/span'))
            )
            account_password_login_btn.click()

            # 等待切换后的页面加载
            time.sleep(2)

            # 这里可以添加后续的登录操作，例如输入用户名和密码
            # 示例：找到用户名输入框并输入用户名
            username_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[1]/fb-header/div[2]/div/div[2]/div[1]/input')))
            username_input.send_keys('18255877595')

            # 定位并输入密码，假设密码输入框的 placeholder 是 "密码"
            password_input = wait.until(
                EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[1]/fb-header/div[2]/div/div[2]/div[2]/input'))
            )
            password_input.send_keys('fanyuqi123')

            # 等待协议勾选框加载
            time.sleep(2)
            # 定位协议勾选框，这里假设其 xpath 为示例值，需根据实际情况修改
            agree_checkbox = wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[1]/fb-header/div[2]/div/div[2]/div[6]/div[1]'))
            )
            # 点击勾选协议
            agree_checkbox.click()
            print("已勾选同意协议")

            # 找到登录提交按钮并点击，假设提交按钮有特定的文本
            submit_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[1]/fb-header/div[2]/div/div[2]/div[4]/div/div'))
            )
            submit_button.click()
            # 等待登录完成
            time.sleep(10)
            print("登录操作完成")

        except:
            # 未找到登录按钮，认为已经登录成功
            print("未找到登录按钮，可能已登录成功")

    except Exception as e:
        print(f"An login error occurred: {e}")
