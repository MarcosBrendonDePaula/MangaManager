import os
import os.path
import base64
import pickle
import cloudscraper

import tarfile
from tqdm import tqdm

class Chapter:
    def __init__(self,Name = "",Number = 0,Lang="ptbr",path="/"):
        self.Name   = Name
        self.Number = Number
        self.Pages  = []
        self.Lang   = Lang
        self.directory = path+"/"+base64.b64encode(str(Name+str(Number)+Lang).encode('ascii')).decode('ascii')
        self.__CheckOrCreateFolder__()

    def __CheckOrCreateFolder__(self):
        try:
            if os.path.exists(self.directory):
                obj = open(self.directory+"/obj.cap", "rb")
                temp = pickle.load(obj)
                self.Name   = temp.Name
                self.Number = temp.Number
                self.Pages  = temp.Pages
                self.Lang   = temp.Lang
                obj.close()
                pass
            else:
                os.mkdir(self.directory)
                os.mkdir(self.directory + "/temp")
                self.__UpdateObj__()
        except:

            pass

    def __UpdateObj__(self):
        obj = open(self.directory + "/obj.cap", "wb")
        pickle.dump(self, obj)
        obj.close()

    def UnpackPages(self):
        try:
            tar = tarfile.open(self.directory + "/files.tar.gz", mode="r:gz")
            members = tar.getmembers()
            progress = tqdm(members)
            for member in progress:
                tar.extract(member, path=self.directory + "/temp")
                progress.set_description(f"Extracting {member.name}")
            tar.close()
            return self.directory + "/temp"
        except:
            return
        pass

    def PackPages(self):
        tar = tarfile.open(self.directory+"/files.tar.gz", mode="w:gz")
        members = []
        for i in self.Pages:
            tar.add(self.directory+"/temp/"+i, i)
        tar.close()
        for i in self.Pages:
            os.remove(self.directory+"/temp/"+i)
        pass

    def AddPage(self,img_link):
        self.UnpackPages()
        scraper = cloudscraper.create_scraper(browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': False
        })
        r = scraper.get(img_link)
        print(self.directory)
        with open(self.directory+"/temp/"+str(len(self.Pages))+".jpg", 'wb') as f:
            f.write(r.content)
            f.close()

        self.Pages.append(str(len(self.Pages))+".jpg")
        self.__UpdateObj__()
        self.PackPages()
        pass