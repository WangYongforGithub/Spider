"""
#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Project_Describe: 
爬取成都链家二手房前5页信息, 网页中每页有30个住房信息
# @Author  : WY
# @File    : chengdu_lianjia_hand_house.py
# @Software: PyCharm
# @Date    : 2021/10/20 20:51
"""

from selenium import webdriver
import csv

with open('成都链家二手房信息.csv', 'a+', newline='', encoding='utf-8') as file:
    write = csv.writer(file)
    write.writerow(['标题', '地址', '房源信息', '总价', '单价'])

for i in range(1, 11):
    url = 'https://cd.lianjia.com/ershoufang/pg1/'

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    wb = webdriver.Chrome(options=option)
    wb.get(url)

    title = wb.find_elements(by='xpath', value='/html/body/div[4]/div[1]/ul/li/div[1]/div[1]/a')
    address = wb.find_elements(by='xpath', value='/html/body/div[4]/div[1]/ul/li/div[1]/div[2]/div')
    info = wb.find_elements(by='xpath', value='/html/body/div[4]/div[1]/ul/li/div[1]/div[3]/div')
    total_price = wb.find_elements(by='xpath', value='/html/body/div[4]/div[1]/ul/li/div[1]/div[6]/div[1]')
    unit_price = wb.find_elements(by='xpath', value='/html/body/div[4]/div[1]/ul/li/div[1]/div[6]/div[2]')

    titles = []
    addresses = []
    infos = []
    total_prices = []
    unit_prices = []

    for i in range(len(title)):

        titles.append(title[i].text)
        infos.append(info[i].text)
        addresses.append(address[i].text)
        total_prices.append(total_price[i].text.replace('\n', ''))
        unit_prices.append(unit_price[i].text)

    with open('成都链家二手房信息.csv', 'a+', newline='', encoding='utf-8') as file:
        for num in range(len(titles)):
            write = csv.writer(file)
            write.writerow([titles[num], addresses[num], infos[num], total_prices[num], unit_prices[num]])

    wb.quit()