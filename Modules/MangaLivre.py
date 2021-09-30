
from Modules.Module import *

class MangaLivre(Module):
    def __UpdateInfo__(self, manga_link="", type="Manhua", path=os.getcwdb().decode("ascii")):
        scraper = cloudscraper.create_scraper(browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': False
        })
        r = scraper.get(manga_link)
        scrap = BeautifulSoup(r.content,'html.parser')

        infos = scrap.find(id="series-data")

        Name = infos.find(class_="series-info").find(class_="series-title").find("h1").text.lower()
        if Name[-1] == " ":
            Name = Name[:-1]
        Name = Name.replace("\n","")
        
        capterlist = scrap.find(id="chapter-list")
        
        Caps = []
        for cap in capterlist.find(class_="list-of-chapters").find_all("li"):
            Caps.append((str(cap.find("a").attrs["title"]).split("Ler Capítulo ")[1],cap.find("a").attrs["href"]))
        
        Img = infos.find(class_="series-img").find("img").attrs["src"]

        Desc = scrap.find(class_="series-desc").find("span").find("span").text
        
        Genre = []
        for genre in scrap.find(class_="touchcarousel-wrapper").findAll("touchcarousel-item"):
            Genre.append(genre.find("a").find("span").text)
        
        manga = Manga(Name,path)
        manga.__ImgDownload__(Img)
        manga.Chapters = Caps
        manga.Desc = Desc
        manga.Genre = Genre
        manga.type = type
        manga.module = MangaLivre()
        manga.__UpdateObj__()
        pass
    pass