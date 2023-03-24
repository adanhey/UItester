import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from tools import *
from logger import *


class PageObject:
    def __init__(self, browser='Chrome', wait_time=10, interval_time=1):
        self.logger = TestLogger()
        self.browser = eval(f"webdriver.{browser}()")
        self.logger.log_event("当前使用的浏览器：", browser)
        self.waiter = WebDriverWait(self.browser, wait_time, interval_time)
        self.currentElement = None
        self.today = datetime.datetime.now().strftime("%Y-%m-%d")
        self.execTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        os.mkdir("./mission%s" % self.execTime)

    def get_url(self, url, login_dict=None):
        self.logger.log_event("获取url", url)
        self.browser.get(url)
        self.browser.maximize_window()
        if login_dict:
            self.enter_word(login_dict['accountXpath'], login_dict['account'])
            self.enter_word(login_dict['passwordXpath'], login_dict['password'])
            if 'loginExtend' in login_dict:
                self.click(login_dict['loginExtend'])
            self.click(login_dict['loginButton'])

    def wait_and_find(self, value, by='xpath', is_need_wait=0.2):
        self.logger.log_event("通过%s获取元素" % by, value)
        self.waiter.until(lambda browser: browser.find_element(by=by, value=value))
        element = self.browser.find_element(by=by, value=value)
        self.currentElement = element
        if is_need_wait > 0:
            time.sleep(is_need_wait)
            self.logger.log_event(f"停留{is_need_wait}秒")
        return element

    def click(self, element_path, actionDict=None, title=None, *args):
        self.logger.log_event(f"点击事件：{title}")
        element = self.wait_and_find(element_path)
        element.click()

    def enter_word(self, element_path, actionDict, title=None, *args):
        self.logger.log_event(f"写入事件：{title}, 写入值", actionDict['sendWord'])
        element = self.wait_and_find(element_path)
        element.clear()
        element.send_keys(actionDict['sendWord'])

    def switch_frame(self, element_path, actionDict=None, title=None, *args):
        if element_path == 'default':
            self.logger.log_event("切换到默认frame")
            self.browser.switch_to.default_content()
        else:
            self.logger.log_event(f"切换frame事件：{title}")
            element = self.wait_and_find(element_path)
            self.browser.switch_to.frame(element)

    def switch_handle(self, element_path, actionDict=None, title=None, *args):
        handles = self.browser.window_handles
        current_handle = self.browser.current_window_handle
        self.logger.log_event(f"切换页面：{title}")
        if element_path == "last":
            for i in range(len(handles)):
                if handles[i] == current_handle:
                    self.browser.switch_to.window(handles[i - 1])
                    break
        elif element_path == 'next':
            for i in range(len(handles)):
                if handles[i] == current_handle:
                    self.browser.switch_to.window(handles[i + 1])
                    break
        else:
            self.browser.switch_to.window(handles[element_path])

    def element_check(self, element_type="value"):
        pass

    def save_screen(self, caseNo, title, screenshot_wait=0.2):
        time.sleep(screenshot_wait)
        self.logger.log_event(f"保存事件：{title}截图")
        self.browser.save_screenshot(f"./mission{self.execTime}/{caseNo}/{title}.png")
        return f"./mission{self.execTime}/{caseNo}/{title}.png"

    def scroll_to(self, element_path=None, actionDict=None, title=None, *args):
        self.logger.log_event(f"滑动屏幕：x轴{actionDict['x']}px,y轴{actionDict['y']}px")
        self.browser.execute_script(f"window.scrollBy({actionDict['x']}, {actionDict['y']})")

    def close_browser(self):
        self.browser.close()
