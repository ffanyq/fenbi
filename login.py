from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_main(url):
    # 如果你没有将ChromeDriver添加到系统PATH中，可以指定其路径
    # service = Service('path/to/chromedriver')
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome()
    # driver.set_window_size(1024, 30000)
    # driver.maximize_window()
    try:
        # 打开登录页面
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        #登录按钮
        try:
            # body > app-root > div > div.fenbi-web-header > fb-header > div > div.info-wrapper > button
            #找登录按钮#fb-web-nav-header > div > div > button
            login_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#fb-web-nav-header > div > div > button'))
            )

            # 找到登录按钮，点击它
            login_button.click()
            # 等待登录页面加载
            time.sleep(3)

            # 查找并点击“账号密码登录”切换按钮/html/body/fb-code-login-modal/div/main/div[2]/form/div[5]/button
            account_password_login_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/fb-code-login-modal/div/main/div[2]/form/div[5]/button'))
            )
            account_password_login_btn.click()

            # 等待切换后的页面加载
            time.sleep(2)

            # 这里可以添加后续的登录操作，例如输入用户名和密码
            # 示例：找到用户名输入框并输入用户名/html/body/fb-code-login-modal/div/main/div[2]/form/div[1]/input
            username_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/fb-login-modal/div/main/div[2]/form/div[1]/input')))
            username_input.send_keys('18255877595')

            # 定位并输入密码，假设密码输入框的 placeholder 是 "密码"
            password_input = wait.until(
                EC.presence_of_element_located((By.XPATH, '/html/body/fb-login-modal/div/main/div[2]/form/div[2]/input'))
            )
            password_input.send_keys('fanyuqi123')

            # 等待协议勾选框加载
            time.sleep(2)
            # 定位协议勾选框，这里假设其 xpath 为示例值，需根据实际情况修改
            agree_checkbox = wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/fb-login-modal/div/main/div[2]/div[2]/div[1]'))
            )
            # 点击勾选协议
            agree_checkbox.click()
            print("已勾选同意协议")

            # 找到登录提交按钮并点击，假设提交按钮有特定的文本
            submit_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/fb-login-modal/div/main/div[2]/form/div[4]/button'))
            )
            submit_button.click()
            print("登录操作完成")

            # 等待登录完成
            time.sleep(5)


            #退到历史主页
            tiku_home = wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-main/div[2]/app-real-test/header/app-simple-nav-left-header/header/div/a/span'))
            )
            tiku_home.click()
            time.sleep(2)

            #点击历史主页
            history_home = wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-main/div[2]/app-catalog/div/main/div[2]/div[1]/app-history-catalog/div/div[1]/a'))
            )
            history_home.click()
            time.sleep(2)

            #/html/body/app-root/div/app-main/div[2]/app-report-profile/div/main/app-history/div/article/div[18]/div[2]/div[2]/span
            #/html/body/app-root/div/app-main/div[2]/app-report-profile/div/main/app-history/div/article/div[10]/div[2]/div[2]/span
            div_index = 1


            while True:
                try:
                    x_path = '/html/body/app-root/div/app-main/div[2]/app-report-profile/div/main/app-history/div/article/div[%d]/div[2]/div[2]/span'
                    x_path = x_path % div_index
                    print(x_path)
                    t_element = driver.find_element(By.XPATH, x_path)
                    print('000000')
                    driver.execute_script("arguments[0].scrollIntoView();", t_element)
                    print('11111111')
                    div_index = div_index + 5
                    print('2222222')
                    time.sleep(3)
                    print('33333333')
                except NoSuchElementException:
                    print('未找到元素，跳出循环')
                    break
                except Exception as e:
                    print(f"发生其他异常: {e}")
                    break
            print('移动结束')
            time.sleep(20)
            # while True:
            #     print('滚动')
            #
            #     # 滚动到页面底部
            #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #
            #     # 等待页面加载新内容
            #     time.sleep(2)  # 可根据实际情况调整等待时间
            #
            #     # 获取新的页面高度
            #     new_height = driver.execute_script("return document.body.scrollHeight")
            #     print(new_height)
            #
            #     # 判断页面高度是否有变化
            #     if new_height == last_height:
            #         break
            #
            #     # 更新页面高度
            #     last_height = new_height
            print("页面内容已全部加载")

        except:
            # 未找到登录按钮，认为已经登录成功
            print("未找到登录按钮，可能已登录成功")

    except Exception as e:
        print(f"An login error occurred: {e}")
