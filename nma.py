# -*- coding: utf-8 -*-

import requests
import os

try:
    import wget
except:
    os.system("pip install wget")
    import wget
    print("please chech wget library")

def get_url():
    listt=[]
    file = open("urllist.txt", "r")
    url_list=file.read().strip().split("\n")[1:]
    for url in url_list:
        response = str(requests.request('GET',url)._content).split("href=")
        for item in response:
            a=item.split('"')[1]
            if "ipynb" in a and ".." not in a and "nbviewer" not in a and "NeuromatchAcademy" in a:
                a="https://raw.githubusercontent.com"+a.split("github")[1].split("/blob")[0]+a.split("github")[1].split("/blob")[1]
                listt.append(a)
    print("getting urls has finished...")
    file = open("url.txt", "w")
    for item in listt:
        file.write(item+"\n")
    file.close()
    return listt


file2 = open("url.txt", "r")
a=file2.read().split("\n")
if len(a)<2:
    item_list=get_url()
    print("url recording to text file has finished...")
else:
    item_list=set(a[:-1])
file2.close()
print("start downloading...")
os.mkdir(str(os.getcwd())+"\_files")
for item in item_list:
    path=str(os.getcwd())+"\_files"+"\_"+str(item).split("/")[-1]
    try:
        wget.download(item,path)
    except:
        print(item.split("/")[-1]," cannot be downloaded...")
print("downloading files from urls has finished...")




