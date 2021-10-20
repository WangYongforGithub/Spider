"""
#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Project_Describe: 
刷csdn浏览量，这个版本只适合该网址不存在展示活动的时候
# @Author  : WY
# @File    : example01.py
# @Software: PyCharm
# @Date    : 2021/9/4 15:29
"""
import time

from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

url = 'https://blog.csdn.net/qq_51136340?spm=1000.2115.3001.5343'


def brush_views(url=url):
    try:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        wb = webdriver.Chrome(options=option)
        # wb = webdriver.Chrome()
        wb.get(url)
        # 设置显示等待
        wb.implicitly_wait(10)
        titles = wb.find_elements_by_xpath('//*[@id="floor-user-profile_485"]/div/div[2]/div/div[2]/div/div[2]/div/div/div')
        # print('程序开始加载....')
        # time.sleep(1)

        for i in tqdm(range(1, len(titles)+1), desc='加载中'):
            brush(i, wb)
            time.sleep(1)

    except Exception as err:
        print(err)
    finally:
        # print('程序结束！')
        wb.quit()


def brush(i, wb):
    wb.find_element_by_xpath(f'//*[@id="floor-user-profile_485"]'
                             f'/div/div[2]/div/div[2]/div/div[2]/div/div/div[{i}]').click()
    windows = wb.window_handles
    wb.switch_to.window(windows[-1])
    time.sleep(1)
    # max_y = 6000
    # y = 0
    # while y <= max_y:
    #     wb.execute_script(f'window.scrollTo(0, {y})')
    #     # time.sleep(1)
    #     y += 2000
    wb.switch_to.window(windows[0])
    # time.sleep(1)


if __name__ == '__main__':
    for _ in range(40):
        brush_views()
        time.sleep(2)

