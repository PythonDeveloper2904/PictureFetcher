#!/usr/bin/env python
# -*- coding:utf-8 -*-

import bs4
import colorama
import os
import requests
from tqdm import tqdm

def get_response(url)->bs4.BeautifulSoup|None:
    """
    发送请求并返回解析后的HTML内容
    :param url: 请求的URL
    :return: BeautifulSoup对象, 如果请求失败则返回None
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查是否请求成功
        return bs4.BeautifulSoup(response,parser="html.parser")
    except requests.RequestException as e:
        print(colorama.Fore.RED+f"请求错误: {e}"+colorama.Style.RESET_ALL)
        return None

def fetch_pictures(soup:bs4.BeautifulSoup)->list|None:
    """

    :param soup:
    :return:
    """
    pass

def save_pictures():
    pass

def main():
    global url,word,number,folder  # 将这四个变量设为全局变量
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
    url+=word
    soup = get_response(url)

if __name__=="__main__":
    url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=&st=-1&fm=index&hs=0&xthttps=111110&sf=1&ic=0&nc=1&showtab=0&fb=0&face=0&istype=2&ie=utf-8&word="
    word = None
    number = None
    folder = None
    soup = None
    main()
