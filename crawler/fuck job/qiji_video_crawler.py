from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginAutomation:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url

    def login(self, username, password):
        try:
            # 打开登录页面
            self.driver.get(self.url)

            # 等待页面加载完成
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "el-input__inner"))
            )

            # 找到所有 class=el-input__inner 的元素
            input_elements = self.driver.find_elements(By.CLASS_NAME, "el-input__inner")

            if not input_elements:
                print("未找到任何输入框元素")
                return
            # 假设第一个 el-input__inner 是用户名输入框，第二个是密码输入框
            if len(input_elements) < 2:
                print("找到的输入框元素不足两个")
                return

            username_input = input_elements[0]
            username_input.send_keys(username)

            password_input = input_elements[1]
            password_input.send_keys(password)

            # 找到复选框点击
            checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "el-checkbox__input"))
            )
            checkbox.click()

            # 找到 login-btn 下的第一个 button 并点击
            login_btn_div = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-btn"))
            )
            login_buttons = login_btn_div.find_elements(By.TAG_NAME, "button")

            if not login_buttons:
                print("未找到任何 login-btn 下的 button 元素")
                return

            # 假设第一个 button 是“立即登录”按钮
            if len(login_buttons) < 1:
                print("找到的 login-btn 下的 button 元素不足一个")
                return

            login_button = login_buttons[0]
            login_button.click()
            # 等待几秒钟以查看结果
            time.sleep(10)
            # 截取屏幕截图并保存到指定路径
            screenshot_path = r"C:\Users\XG1001001\Downloads\screenshot.png"
            self.driver.save_screenshot(screenshot_path)
            print(f"截图已保存到 {screenshot_path}")
        except Exception as e:
            print(f"发生错误: {e}")

    def close_browser(self):
        # 关闭浏览器
        self.driver.quit()

# 使用示例
if __name__ == "__main__":
    login_url = "https://vtest.qiji.video/#/login"
    username = "testceo"
    password = "zh123456!"

    # login_url="https://vdq.qiji.video/#/"
    # username="大旗产品"
    # password="dq,123456"

    login_automation = LoginAutomation(login_url)
    login_automation.login(username, password)
    login_automation.close_browser()
