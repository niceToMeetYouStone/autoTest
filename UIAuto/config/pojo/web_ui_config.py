# -*- coding: utf-8 -*-
"""
====================================
@File Name ：read_web_ui_config.py
@Time ： 2022/10/31 11:31
@Program IDE ：PyCharm
@Create by Author ： stone
@Describe：web UI 配置文件对象类
====================================
"""


class WEB_UI_Config:
    def __init__(self):
        self.selenium_hub = None
        self.test_workers = None
        self.test_browsers = []
        self.current_browser = None
        self.download_dir = None
        self.is_chrome_headless = None
        self.is_firefox_headless = None
