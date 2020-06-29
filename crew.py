#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
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
 
while(True):
        req=input("Dán link tại đây: ")
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

        tieude=convert(tacgia)+"_"+convert(tit).replace(':','-')+"-Spiderum.txt" 
        file = open(tieude, "wb")
        tit=tit.encode()
        tacgia="Tác giả: "+tacgia
        file.write(tit+t.encode()+tacgia.encode())
        file.close()
        print("Done!!")

 

