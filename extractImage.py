from bs4 import BeautifulSoup
import requests
import os
import urllib.request
from time import sleep

class ImageDownload():
    web_url=""
    url=""
    img_name=""
    data=""
    img_tags=""
    imglen=""
    create_dir=""
    count=0
    img_dic=dict()
    #Taking input from user as Website URL    
    #step 1
    def __init__(self):
        self.url=input('Enter the URL for webpage:')
        #url="w3school.com"
        self.web_url="http://"+self.url
        #print(self.web_url)
        #get website name to create directory
        dirname=self.get_webname()
        # check path of current working directory
        path=os.getcwd()
        #combine path and directory name to create directory path name
        self.create_dir=path+"/"+dirname
        check=os.path.isdir(self.create_dir)
        #check if directory exists,if not create directory
        if not check:
            os.mkdir(self.create_dir)
        self.url_data()
        
        
    #GEt the image name from path of URL to specified image
    #step 6
    def get_imagename(self,path):
        #get_image name
        img_name=path.split('/')
        return img_name[-1]
        
        
    #downloading images from URL
    #step 5
    def downloader(self,image_url):
        #file_name = random.randrange(1,10000)
        full_file_name =self.get_imagename(image_url)
        urllib.request.urlretrieve(image_url,self.create_dir+"/"+full_file_name)
        print(str(self.count)+' Downloaded ---'+full_file_name)
        sleep(2)
        
    #getWebsite name
    def get_webname(self):
        webname=self.url.split('.')
        return webname[0]
    
    
    
    
    
    #get data as html from URL
    def image_dict(self):
        imagepath=self.web_url+"/"
        imglist=list()
        #storing image URLs of selected website
        for i in self.img_tags:
            imglist.append(i['src'])
        self.imglen=len(imglist)+1
        
        
        self.img_dic={i:imagepath+v for (i,v) in zip(range(0,len(imglist)),imglist)}
        
   
    def get_imglen(self):
        return self.imglen
    #Parse the data to get specified tag here it is image         
    #step 3       
    
    
    def parse_web(self):
        html=BeautifulSoup(self.data,'lxml')
        self.img_tags=html.find_all('img')
        self.image_dict()
    
    def url_data(self):
    #step 2
        try:
            r=requests.get(self.web_url)
            self.data=r.text
            #print(self.data)
            self.parse_web()
        except:
            print('URL error')
            
    def download(self):
        for i in self.img_dic:
            self.downloader(self.img_dic[i])
            self.count=i+1
            
            
                
    #Converting list of image tag to (key,value) pair where key=0 to len(h) value=imagepath
    #step 4
    
    
    
website=ImageDownload()
website.download()




