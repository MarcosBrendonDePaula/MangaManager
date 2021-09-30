from Modules.Module import *

class Neox(Module):
    def __init__(self):
        pass

    def __CapDownloader__(self,manga,cap_link,capNum=0):
        scraper = cloudscraper.create_scraper(browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': False
        })

        r = scraper.get(cap_link)
        scrap = BeautifulSoup(r.content, 'html.parser')
        divs = scrap.findAll("div",class_="page-break")
        for div in divs:
            img = div.find("img").attrs["data-src"]
            manga.GetCap(capNum).AddPage(img)
        pass
    
    def __UpdateInfo__(self,manga_link="",type="Manhua",path = os.getcwdb().decode("ascii")):
        scraper = cloudscraper.create_scraper(browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': False
        })
        r = scraper.get(manga_link)
        scrap = BeautifulSoup(r.content,'html.parser')

        Name = scrap.find(class_="post-title").find("h1").text.lower()
        if Name[-1] == " ":
            Name = Name[:-1]
        Name = Name.replace("\n","")
        Caps = []
        for cap in scrap.find_all(class_="wp-manga-chapter"):
            Caps.append((str(cap.find("a").text).split("Cap. ")[1],cap.find("a").attrs["href"]))
        Img = scrap.find(class_="summary_image").find("img").attrs["data-src"]
        Desc = scrap.find(class_="summary__content").find("p").text
        Genre = []
        for genre in scrap.find(class_="genres-content").findAll("a"):
            Genre.append(genre.text)
        manga = Manga(Name,path)
        manga.__ImgDownload__(Img)
        manga.Chapters = Caps
        manga.Desc = Desc
        manga.Genre = Genre
        manga.type = type
        manga.module = Neox()
        manga.__UpdateObj__()

