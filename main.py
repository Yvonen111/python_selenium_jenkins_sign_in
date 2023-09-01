import time


def login_page(username, password, driver, By):  # 登录页面
    # driver.find_element(By.XPATH, '//input[@autocomplete="username"]').send_keys(username)
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//input[@autocomplete="current-password"]').send_keys(password)
    # time.sleep(2)
    # driver.find_element(By.XPATH, '//i[@class="icon icon-nocheck"]').click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, '//button[@class="base-button"]').click()
    # time.sleep(1)

    driver.find_element(By.ID, 'jinsom-pop-username').send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, 'jinsom-pop-password').send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH, '//div[@class="jinsom-reg-doc"]/input').click()
    driver.find_element(By.XPATH, '//div[@class="jinsom-login-btn"]/span[@class="login opacity"]').click()


def open_url(url, driver):  # 打开页面
    driver.get(url)
    driver.maximize_window()


def search_key(url, driver, username, password, By):
    open_url(url, driver)
    # driver.find_element(By.ID,id='switcher_plogin')
    time.sleep(1)


    # iframe1=driver.find_element(By.XPATH ,'//iframe[@class ="QQMailSdkTool_login_loginBox_qq_iframe"]')   # 连续切换两个窗口
    # driver.switch_to.frame(iframe1)
    # print("切换成功1")
    # iframe2 = driver.find_element(By.XPATH, '//iframe[@id="ptlogin_iframe"]')
    # driver.switch_to.frame(iframe2)
    # print("切换成功2")
    # driver.find_element(By.XPATH,'//a[@id="switcher_plogin"]').click()

    driver.find_element(By.XPATH, '//div[@id="ampHasNoLogin"]').click()

    # iframe1=driver.find_element(By.XPATH ,'//iframe[@name="passport_iframe"]')        # 切换窗口
    # driver.switch_to.frame(iframe1)
    # print("切换成功1")
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//span[text()="密码登录"]').click()

    login_page(username, password, driver, By)
    print("登陆成功")

    # driver.switch_to.parent_frame()

    result = []                 # 打印网页标题
    page_tite = driver.title
    result.append(page_tite)
    return result

def is_exit(element,driver,By):
    flag = True
    try:
        driver.find_element(By.XPATH,element)
        return flag

    except:
        flag = False
        return flag

if __name__ == '__main__':
    # 1、导入库文件
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    driver = webdriver.Edge()
    driver.implicitly_wait(10)

    # 2、数据设置
    url = ['http://ehall.cqupt.edu.cn/new/index.html ',
           'https://yftk.fun/imcoming/']  # https://www.csdn.net/   https://mail.qq.com/  http://ehall.cqupt.edu.cn/new/index.html

    login_date = [["3116567","Yvonne11","15730036613"],
                  ["shmily49359"]]  # 多个元组


    # 3、调用函数
    # 1）将参数先取出来
    url =url[1]  # 调用某个函数里面的 某个元组
    user = login_date[0][2]
    pwd = login_date[1][0]

    # 2） 传参  调用函数
    # 打开网页
    open_url(url, driver)
    print("打开成功")
    time.sleep(1)

    driver.find_element(By.XPATH, '//li[@class="login opacity"]').click()

    # 登录网页
    login_page(user, pwd, driver, By)
    print("登陆成功")

    # 打印网页标题
    result = []
    page_tite = driver.title
    result.append(page_tite)
    print(result)

    # 签到
    try:
        driver.find_element(By.XPATH, '//div[@class="jinsom-sign-page-btn had opacity"]')
        print("今日已签到")
    except:
        driver.find_element(By.XPATH, '//i[@class="jinsom-icon jinsom-qiandao3"]').click()
        print("签到成功")

    driver.refresh()
    time.sleep(2)

    day_num = driver.find_element(By.XPATH, '//div[@class="jinsom-sign-page-month-days"]/span').get_attribute('innerText')
    print("本月签到{}天".format(day_num))

    if 3 <= int(day_num) < 7 :
        driver.find_element(By.XPATH, '//div[@onclick="jinsom_sign_treasure(0,this)"]').click()
        print("已领取第一个宝箱")
    elif 7 <= int(day_num) < 15:
        driver.find_element(By.XPATH, '//div[@onclick="jinsom_sign_treasure(1,this)"]').click()
        print("已领取第二个宝箱")
    elif 15 <= int(day_num) < 28:
        driver.find_element(By.XPATH, '//div[@onclick="jinsom_sign_treasure(2,this)"]').click()
        print("已领取第三个宝箱")
    elif 28 <= int(day_num) < 31:
        driver.find_element(By.XPATH, '//div[@onclick="jinsom_sign_treasure(3,this)"]').click()
        print("已领取第四个宝箱")
    elif 31 <= int(day_num) :
        print("系统出差！")
    print("签到完成！！！！！！！！！！！！")



