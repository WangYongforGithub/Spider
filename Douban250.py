"""
#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Project_Describe: 

# @Author  : WY
# @File    : Douban250.py
# @Software: PyCharm
# @Date    : 2021/10/20 19:59
"""

from selenium import webdriver
import csv
from tqdm import tqdm


def crawling_moive():
    # 先新建csv文件用于存储数据
    with open('豆瓣电影TOP250.csv', 'a+', newline='', encoding='utf-8') as file:
        write = csv.writer(file)
        write.writerow(['电影名称', '评分', '电影热评'])

    for i in range(10):
        url = f'https://movie.douban.com/top250?start={i * 25}&filter='
        # wb = webdriver.Chrome()
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        wb = webdriver.Chrome(options=option)
        wb.get(url)

        movie_title = []  # 电影名
        movie_score = []  # 电影评分
        movie_Hot_comment = []  # 电影热评

        length = wb.find_elements(by='xpath',
                                  value='/html/body/div[3]/div[1]/div/div[1]/ol/li')

        for i in range(1, len(length) + 1):
            movie_title.append(wb.find_element(by='xpath',
                                               value=f'/html/body/div[3]/div[1]/div/div[1]/ol/li[{i}]/div/div[2]/div[1]/a/span[1]').text)
            try:
                movie_score.append(wb.find_element(by='xpath',
                                                   value=f'/html/body/div[3]/div[1]/div/div[1]/ol/li[{i}]/div/div[2]/div[2]/div/span[2]').text)
            except Exception:
                movie_score.append('None')
            try:
                movie_Hot_comment.append(wb.find_element(by='xpath',
                                                         value=f'/html/body/div[3]/div[1]/div/div[1]/ol/li[{i}]/div/div[2]/div[2]/p[2]/span').text)
            except Exception:
                movie_Hot_comment.append('None')

        # 写入文件
        with open('豆瓣电影TOP250.csv', 'a+', newline='', encoding='utf-8') as file:
            write = csv.writer(file)
            for num in range(len(movie_title)):
                write.writerow([movie_title[num], movie_score[num], movie_Hot_comment[num]])

        wb.quit()


if __name__ == '__main__':
    print('正在进行中....')
    crawling_moive()
    print('任务已完成！！')
