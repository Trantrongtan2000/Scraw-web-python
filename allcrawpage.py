#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import sys

patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}

def convert(text):
    """
    Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'

    text: input string to be converted

    Return: string converted
    """
    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output
dem=0 
trang=input("Nhập số trang cần lấy: ")
for i in range(1,int(trang)+1):
    html_page = urllib.request.urlopen("https://spiderum.com/s/science2vn/hot?page="+str(i))
    link = BeautifulSoup(html_page, "html.parser")
    for link in link.findAll('a',attrs={'href': re.compile("^/bai-dang/"),'class':'body'}):
        a=link.get('href')   
        page="https://spiderum.com"+a     
        req=page
        req = requests.get(req)
        soup = BeautifulSoup(req.text, "lxml")
        for tag in soup.find_all('a', attrs={"fragment": "profile"}):
                tacgia=tag.getText()
                tacgia=tacgia.strip()
        for tag in soup.find_all('h1'):
                tit=tag.getText()
                tit=tit.strip()

        for tag in soup.find_all('div', attrs={"class": "content"}):
                t=tag.getText()
                t=t.replace('.','.\n')

        tieude=convert(tacgia).replace('?','')+"_"+convert(tit).replace(':','-').replace('?','').replace('"','-').replace('/','phan').replace('\n','').replace('*','').replace('|','')+"-Spiderum.txt" 
        file = open("C:/Users/Admin/Desktop/crew bao python/news-crawler/spiderum/"+tieude, "wb")
        tit=tit.encode()
        tacgia="Tác giả: "+tacgia
        file.write(tit+t.encode()+tacgia.encode())
        file.close()
        dem+=1
        print(tieude) 
    print("Trang "+str(i))
print("Hoàn thành!!! Số file đã tạo là: ",dem)

 

