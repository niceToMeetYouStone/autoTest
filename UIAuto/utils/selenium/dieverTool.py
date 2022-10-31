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
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.ie import webdriver as ie_webdriver
from UIAuto.config.utils.read_web_ui_config import Read_WEB_UI_Config


class DriverTool:

    @classmethod
    def get_driver(cls, selenium_sub, browser_type) -> webdriver:
        driver = None
        browser_type = browser_type.lower()
        download_file_content_types = "application/octet-stream,application/vnd.ms-excel,text/csv,application/zip,application/binary"

        if browser_type == 'ie':
            opt = ie_webdriver.Options()
            # 强制使用createProcessApi启动浏览器
            opt.force_create_process_api = True
            opt.ensure_clean_session = True
            opt.add_argument('-private')
            ie_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
            ie_capabilities.update(opt.to_capabilities())
            driver = webdriver.Remote(selenium_sub, desired_capabilities=ie_capabilities)
        elif browser_type == 'firefox':
            firefox_profile = FirefoxProfile()
            # firefox_profile参数可以在浏览器中访问about：config进行查看
            firefox_profile.set_preference('browser.download.folderList', 2)  # 0 是桌面，1是我的下载，2是自定义
            firefox_profile.set_preference('browser.download.dir', Read_WEB_UI_Config().web_ui_config.download_dir)
            firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', download_file_content_types)
            firefox_options = Firefox_Options()
            if Read_WEB_UI_Config().web_ui_config.is_firefox_headless.lower() == 'true':
                firefox_options.add_argument('--headless')
            firefox_options.profile = firefox_profile
            driver = webdriver.Remote(selenium_sub, webdriver.DesiredCapabilities.FIREFOX.copy(),
                                      options=firefox_options)
        elif browser_type == 'chrome':
            chrome_options = Chrome_Options()
            prefs = {'download.default_directory': Read_WEB_UI_Config().web_ui_config.download_dir,
                     'profile.default_content_settings.popups': 0}
            chrome_options.add_experimental_option('prefs', prefs)
            if Read_WEB_UI_Config().web_ui_config.is_firefox_headless.lower() == 'true':
                chrome_options.add_argument('--headless')
            driver = webdriver.Remote(selenium_sub, webdriver.DesiredCapabilities.CHROME.copy(), options=chrome_options)
        else:
            return driver
        driver.maximize_window()
        driver.delete_all_cookies()
        return driver


if __name__ == '__main__':
    DriverTool.get_driver('127.0.0.1:80', 'ie')
