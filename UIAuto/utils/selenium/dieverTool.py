# -*- coding: utf-8 -*-
"""
====================================
@File Name ：dieverTool.py
@Time ： 2022/10/28 17:18
@Program IDE ：PyCharm
@Create by Author ： stone
@Describe：选择合适的浏览器,返回驱动
====================================
"""
from selenium import webdriver
from selenium.webdriver.ie import webdriver as ie_webdriver


class DriverTool:



    @classmethod
    def get_driver(cls, selenium_sub, browser_type) -> webdriver:
        driver = None
        browser_type = browser_type.lower()
        download_file_content_type = "application/octet-stream,application/vnd.ms-excel,text/csv,application/zip,application/binary"

        if browser_type == 'ie':
            opt = ie_webdriver.Options()
            # 强制使用createProcessApi启动浏览器
            opt.force_create_process_api = True
            opt.ensure_clean_session = True
            opt.add_argument('-private')
            ie_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
            ie_capabilities.update(opt.to_capabilities())
            driver = webdriver.Remote(selenium_sub, desired_capabilities=ie_capabilities)

        driver.maximize_window()
        driver.delete_all_cookies()
        return driver




if __name__ == '__main__':
    DriverTool.get_driver('127.0.0.1:80','ie')