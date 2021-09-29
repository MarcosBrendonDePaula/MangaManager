import pickle
import os
import cloudscraper
from Manga.Cap import Chapter
import base64

class Manga:
    def __init__(self,Name="",path="/"):
        self.Name    = Name
        self.Chapters= []
        self.Desc    = ""
        self.Genre   = []
        self.type    = ""
        self.directory = path+"/"+base64.b64encode(self.Name.encode('ascii')).decode('ascii')
        self.__CheckOrCreateFolder__()

    def GetCap(self,Number,Lang="ptbr"):
        return Chapter(self.Name,Number,Lang,self.directory + "/Chapters")
        pass

    def __ImgDownload__(self,img_link=""):
        try:
            capa = open(self.directory+"/capa.jpg","r")
            print("capa já existe")
            capa.close()
            return
        except:
            pass
        print("fazendo download da capa")
        scraper = cloudscraper.create_scraper(browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': False
        })
        r = scraper.get(img_link)
        with open(self.directory+"/capa.jpg", 'wb') as f:
            f.write(r.content)
            f.close()

    def __CheckOrCreateFolder__(self):
        try:
            if os.path.exists(self.directory):
                print("Abrindo")
                obj = open(self.directory+"/obj.manga", "rb")
                temp = pickle.load(obj)

                self.Name = temp.Name
                self.Chapters = temp.Chapters
                self.Img = temp.Img
                self.Desc = temp.Desc
                self.Genre = temp.Genre
                self.type = temp.type
                obj.close()
                return
                pass
            else:
                print("Criando")
                os.mkdir(self.directory)
                os.mkdir(self.directory + "/Chapters")
                self.__UpdateObj__()
        except:
            pass

    def __UpdateObj__(self):
        obj = open(self.directory +"/obj.manga", "wb")
        pickle.dump(self, obj)
        obj.close()