#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
main.py
Project: PictureFetcher2
Author: PythonDeveloper2904
FirstCommitDate: 2024/10/4
FinalCommitDate: -
"""

import bs4
import colorama
import os
import re  # 导入正则表达式模块
import requests
from tqdm import tqdm

def get_response(url:str)->str|None:
    """
    发送请求并返回解析后的HTML内容
    :param url: 请求的URL
    :return: 网页源代码, 如果请求失败则返回None
    """
    head = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "accept-language":"zh-CN,zh;q=0.9",
        "cookie":"BIDUPSID=3FBC373560F6B1D9EC80226A0CD4825F; PSTM=1724165590; BAIDUID=3FBC373560F6B1D9082AF1AC8303E8F2:FG=1; H_PS_PSSID=60826; H_WISE_SIDS=60826; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=2000a40ka4018g200k2l81ak3hejlj1jfvkkj1u; BAIDUID_BFESS=3FBC373560F6B1D9082AF1AC8303E8F2:FG=1; ZFY=cL0bb97ZEvetMQARzFcDs7F5IAVeM:B0643KCQxCqOs8:C; userFrom=null; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; ab_sr=1.0.1_ODJmZTc0NWU2OGNlNzMyNTE5MTUyNGNhZWVhYTA2YmZkYzkwY2ZmOGRmZGQyYmJhNWVlMDc1OWY4NWQ4NzIyOTUwYjc3NmU4ZjFmZTViMTc5ZjBhMTc4MTc4YTdmODQ1MWUxM2I0MmFmYzc4ODAyYjhlYjcyNjYzN2JjNzVjMDNlOTA5ZDE2MWU3MzQ3NGNiMTcwMDI5ODI5Y2IzYWRjNw==; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm"
    }
    try:
        response = requests.get(url,headers=head)
        response.encoding = "utf-8"  # 将编码设为utf-8
        response.raise_for_status()  # 检查是否请求成功
        return response.text
    except requests.RequestException as e:
        print(colorama.Fore.RED+f"请求错误: {e}"+colorama.Style.RESET_ALL)
        return None

def fetch_pictures(text:str)->list:
    """
    从HTML文本中提取图片的URL
    :param text: HTML文本
    :return: 图片URL列表
    """
    rule = r'"thumbURL": "(.+?)"'  # 通过正则表达式的规则, 匹配符合规则的子串
    lst = re.findall(rule,text)
    for u in lst:
        print(u)
    return lst

def save_pictures():
    pass

def main():
    global url,keyword,number,folder  # 将这四个变量设为全局变量
    url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=&st=-1&fm=index&hs=0&xthttps=111110&sf=1&ic=0&nc=1&showtab=0&fb=0&face=0&istype=2&ie=utf-8&word="
    index = 30
    keyword = None
    number = None
    folder = None
    soup = None
    image_lst = []
    colorama.init()  # 初始化colorama
    keyword = input(colorama.Fore.GREEN+"请输入关键词: "+colorama.Style.RESET_ALL)  # 输入关键词
    number = input(colorama.Fore.GREEN+"请输入图片数量: "+colorama.Style.RESET_ALL)  # 输入图片数量
    folder = (f"./fetch_{keyword}")
    # 判断文件夹是否存在
    if os.path.exists(folder):
        for file in os.listdir(folder):
            os.unlink(f"{folder}/{file}")
    else:
        os.mkdir(folder)
    # 发送请求
    url+=keyword
    soup = get_response(url)
    # 获取图片地址
    temp = fetch_pictures(soup)
    # 把地址存储到列表中
    while number>0:
        url_next_page = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10607818642965054456&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E5%B0%8F%E7%8B%97&queryWord=%E5%B0%8F%E7%8B%97&cl=2&lm=&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn="+str(index)+"&rn=30"
        image_lst.extend(temp[0:number])
        number-=len(temp)
        soup = get_response(url_next_page)
        # 获取下一页
        temp = fetch_pictures(soup)
        index+=30

if __name__=="__main__":
    main()
