from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tinydb import TinyDB, Query
import time

def login_main(url):
    # 如果你没有将ChromeDriver添加到系统PATH中，可以指定其路径
    # service = Service('path/to/chromedriver')
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome()
    db = TinyDB('db.json')
    # driver.set_window_size(1024, 30000)
    # driver.maximize_window()
    try:
        # 打开登录页面
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        #登录按钮
        try:

            #找登录按钮
            login_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#fb-web-nav-header > div > div > button'))
            )

            # 找到登录按钮，点击它
            login_button.click()
            # 等待登录页面加载
            time.sleep(3)

            # 查找并点击“账号密码登录”切换按钮
            account_password_login_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/fb-code-login-modal/div/main/div[2]/form/div[5]/button'))
            )
            account_password_login_btn.click()

            # 等待切换后的页面加载
            time.sleep(2)

            # 这里可以添加后续的登录操作，例如输入用户名和密码
            # 示例：找到用户名输入框并输入用户名
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
            time.sleep(5)

            #点击历史主页
            history_home = wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-main/div[2]/app-catalog/div/main/div[2]/div[1]/app-history-catalog/div/div[1]/a'))
            )
            history_home.click()
            time.sleep(5)

            #循环执行
            div_index = 1
            while True:
                try:

                    x_path = '/html/body/app-root/div/app-main/div[2]/app-report-profile/div/main/app-history/div/article/div[%d]/div[2]/div[1]'
                    data_path = '/html/body/app-root/div/app-main/div[2]/app-report-profile/div/main/app-history/div/article/div[%d]/div[2]/div[2]/span'

                    x_path = x_path % div_index
                    data_path = data_path % div_index
                    print(x_path)

                    #滚动窗口以可见
                    view_element = driver.find_element(By.XPATH, x_path)
                    driver.execute_script("arguments[0].scrollIntoView();", view_element)

                    #记录练习日期
                    date_element = driver.find_element(By.XPATH, data_path)
                    date_text = date_element.text

                    #进入练习页面
                    problem_page = wait.until(
                        EC.element_to_be_clickable((By.XPATH, x_path))
                    )
                    problem_page.click()
                    time.sleep(2)

                    page_title = driver.title
                    category =''
                    if '言语理解与表达' in page_title:
                        category = '言语理解与表达'
                    elif '政治理论' in page_title:
                        category = '政治理论'
                    elif '常识判断' in page_title:
                        category = '常识判断'
                    elif '数量关系' in page_title:
                        category = '数量关系'
                    elif '判断推理' in page_title:
                        category = '判断推理'
                    elif '资料分析' in page_title:
                        category = '资料分析'
                    else:
                        category = '无效'

                    #处理15道题目
                    for problem_index in range(1, 16):
                        db_data = {}
                        db_data['problem_category'] = category
                        db_data['problem_index1'] = div_index
                        db_data['problem_index2'] = problem_index
                        #题目文本
                        problem_text_path = '/html/body/app-root/app-solution/div/app-tis/div/div[%d]/div/app-ti/div/div[2]/app-solution-choice/div/app-question-choice/div/article/p[1]/text()[1]'
                        problem_text_path = problem_text_path % problem_index
                        problem_text_element = driver.find_element(By.XPATH, problem_text_path)
                        problem_text= problem_text_element.text

                        db_data['problem_text'] = problem_text

                        #题目正确与否
                        problem_correct_path = '/html/body/app-root/app-solution/div/app-tis/div/div[%d]/div/app-ti/div/div[1]/div/div[2]'
                        problem_correct_path = problem_correct_path % problem_index
                        problem_correct_element = driver.find_element(By.XPATH, problem_correct_path)
                        problem_color = problem_correct_element.value_of_css_property('color')
                        if problem_color == '#bb312a':
                            problem_is_right = '错误'
                        else:
                            problem_is_right = '正确'
                        db_data['problem_is_right'] = problem_is_right

                        #正确率
                        correct_rate_path_f = '/html/body/app-root/app-solution/div/app-tis/div/div[%d]/div/app-ti/div/div[2]/app-solution-choice/div/app-solution-overall/div/div[3]/span[1]'
                        correct_rate_path_t = '/html/body/app-root/app-solution/div/app-tis/div/div[%d]/div/app-ti/div/div[2]/app-solution-choice/div/app-solution-overall/div/div[2]/span[1]'
                        if problem_is_right == '错误':
                            correct_rate_path = correct_rate_path_f % problem_index
                        else:
                            correct_rate_path = correct_rate_path_t % problem_index

                        correct_rate_element = driver.find_element(By.XPATH, correct_rate_path)
                        correct_rate = correct_rate_element.text
                        db_data['correct_rate'] = correct_rate

                        #耗时
                        time_consuming_path_f = '/html/body/app-root/app-solution/div/app-tis/div/div[%d]/div/app-ti/div/div[2]/app-solution-choice/div/app-solution-overall/div/div[4]/span[1]'
                        time_consuming_path_t = '/html/body/app-root/app-solution/div/app-tis/div/div[%d]/div/app-ti/div/div[2]/app-solution-choice/div/app-solution-overall/div/div[3]/span[1]'
                        if problem_is_right == '错误':
                            time_consuming_path = time_consuming_path_f % problem_index
                        else:
                            time_consuming_path = time_consuming_path_t % problem_index
                        time_consuming_element = driver.find_element(By.XPATH, time_consuming_path)
                        time_consuming = time_consuming_element.text
                        db_data['time_consuming'] = time_consuming

                        db.insert(db_data)


                    div_index = div_index + 1
                    time.sleep(3)
                except NoSuchElementException:
                    print('未找到元素，跳出循环')
                    break
                except Exception as e:
                    print(f"发生其他异常: {e}")
                    break
            print('移动结束')
            time.sleep(20)

            print("页面内容已全部加载")

        except:
            # 未找到登录按钮，认为已经登录成功
            print("未找到登录按钮，可能已登录成功")

    except Exception as e:
        print(f"An login error occurred: {e}")


login_main('https://www.fenbi.com/spa/tiku/guide/catalog/xingce?prefix=xingce')