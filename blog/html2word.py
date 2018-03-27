# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup 
import requests
from PIL import Image
from io import BytesIO

class Html2word(object):
    def __init__(self,html,document):
        self.html = html
        self.document = document    
    def handhtml(self):
        soup = BeautifulSoup(self.html,'html')
        for tag in soup.html.body.contents:
            #先去掉回车符
            if tag != '\n':        
                if tag.name == 'p':
                    p = self.document.add_paragraph('')
                    for child in tag.children:
                        if child.name == 'img':
                                url = child['src']
                                imgName = url.strip().split('/')[-1]
                                self.imgSave(url,imgName)
                                self.document.add_picture(imgName)  # 添加图片 
                        if  hasattr(child,'children'):
                            if child.name == 'strong':
                                #doc接受unicode字符
                                p.add_run(str(child.string).decode('utf-8')).bold = True             
                            if child.name == 'em':
                                p.add_run(str(child.string).decode('utf-8')).italic= True
                        else:
                            p.add_run(str(child).decode('utf-8'))
                if tag.name == 'ul':
                    for child in tag.children:
                        if child!='\n':
                            p = self.document.add_paragraph('',style='List Bullet')
                            for child in child.children:
                                if  hasattr(child,'children'):
                                    if child.name == 'strong':
                                        p.add_run(str(child.string).decode('utf-8')).bold = True
                                    if child.name == 'em':
                                        p.add_run(str(child.string).decode('utf-8')).italic= True
                                else:
                                    p.add_run(str(child).decode('utf-8'))
                if tag.name == 'ol':
                    for child in tag.children:
                        if child!='\n':
                            p = self.document.add_paragraph('',style='List Number')
                            for child in child.children:
                                if  hasattr(child,'children'):
                                    if child.name == 'strong':
                                        p.add_run(str(child.string).decode('utf-8')).bold = True 
                                    if child.name == 'em':
                                        p.add_run(str(child.string).decode('utf-8')).italic= True
                                else:
                                    p.add_run(str(child).decode('utf-8'))       
    def imgSave(self,url,name):
    
        r = requests.get(url)
        i = Image.open(BytesIO(r.content))
        i.save(name)




                        
            