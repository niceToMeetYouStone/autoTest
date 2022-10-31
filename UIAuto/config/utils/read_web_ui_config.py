# -*- coding: utf-8 -*-
"""
====================================
@File Name ：read_web_ui_config.py
@Time ： 2022/10/31 11:16
@Program IDE ：PyCharm
@Create by Author ： stone
@Describe：web UI 测试的参数配置
====================================
"""
import configparser as Configparser
from UIAuto.config.pojo.web_ui_config import WEB_UI_Config


class Read_WEB_UI_Config(object):
    __instance = None
    __inited = None

    # 单例模式
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__inited is None:
            self.web_ui_config = self._readConfig('UIAuto/config/web_ui_config.conf')
            self.__inited = True

    def _readConfig(self, configFile):
        configParser = Configparser.ConfigParser()
        configParser.read(configFile, 'utf-8')
        web_ui_config = WEB_UI_Config()
        web_ui_config.selenium_hub = configParser.get('selenium_server', 'selenium_hub')
        web_ui_config.test_workers = configParser.get('test', 'test_workers')
        web_ui_config.test_browsers = configParser.get('browser', 'test_browser').split("||")
        web_ui_config.current_browser = configParser.get('browser', 'current_browser')
        web_ui_config.download_dir = configParser.get('browser', 'download_dir')
        web_ui_config.is_chrome_headless = configParser.get('browser', 'is_chrome_headless')
        web_ui_config.is_firefox_headless = configParser.get('browser', 'is_firefox_headless')
        return web_ui_config


if __name__ == '__main__':
    print(Read_WEB_UI_Config.web_ui_config)
