"""
#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Project_Describe: 
爬取菜鸟教程python100例
# @Author  : WY
# @File    : example01.py
# @Software: PyCharm
# @Date    : 2021/9/8 20:40
"""
import time

from selenium import webdriver
from tqdm import tqdm
from selenium.webdriver.common.by import By

url = 'https://www.runoob.com/python/python-100-examples.html'


def fetch_100(url=url):
    # 设置浏览器窗口隐藏
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    wb = webdriver.Chrome(options=option)
    # wb = webdriver.Chrome()
    wb.get(url)

    li_lists = wb.find_elements(by=By.CSS_SELECTOR,value='#content > ul:nth-child(3) > li')

    for i in tqdm(range(1, len(li_lists) + 1), desc='进度条'):   # 进度条展示
        wb.implicitly_wait(10)
        wb.find_element(by=By.XPATH, value=f'//*[@id="content"]/ul[1]/li[{i}]/a').click()
        windows = wb.window_handles
        wb.switch_to.window(windows[-1])
        text_title = wb.find_element(by=By.XPATH, value='/html/body/div[4]/div/div[2]/div/div[3]/div/p[2]').text

        text_analysis = wb.find_element(by=By.XPATH, value='/html/body/div[4]/div/div[2]/div/div[3]/div/p[3]').text
        try:
            text_code = wb.find_element(by=By.XPATH, value='//*[@id="content"]/div').text
        except Exception:

            text_code = wb.find_element(by=By.XPATH, value='//*[@id="content"]/pre').text

        with open('100_examples.txt', 'a', encoding='utf-8') as file:
            file.write(f'{i}、{text_title}\n')
            file.write('  ')
            file.write(f'{text_analysis}\n')
            file.write('  ')
            file.write(f'{text_code}\n')
            file.write('\n')
        wb.close()
        wb.switch_to.window(windows[0])

    wb.quit()


if __name__ == '__main__':
    fetch_100()
