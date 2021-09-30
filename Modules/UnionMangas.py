from Modules.Module import *

class Union(Module):
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
        for page in scrap.find_all("img",class_="img-manga"):
            img = page.attrs["src"]
            manga.GetCap(capNum).AddPage(img)
    
    def __UpdateInfo__(self,manga_link="",type="Manhua",path = os.getcwdb().decode("ascii")):
        scraper = cloudscraper.create_scraper(browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': False
        })

        r = scraper.get(manga_link)
        scrap = BeautifulSoup(r.content, 'html.parser')
        # ROW 0 = Titulo
        # ROW 1 = Barra vazia
        # ROW 2 = Informaçoes Manga
        # ROW 3 = Barra vazia
        # ROW 4 = Barra vazia
        # ROW 5 = Barra vazia
        # ROW 6 = Texto Capitulo
        # ROW 7 = Barra vazia
        # Os capitulos contem a classe capitulos 
        rows = scrap.find(class_="perfil-manga").find_all(class_="row")

        Name = str(rows[0].find("h2").text).lower()
        
        if Name[-1] == " ":
            Name = Name[:-1]
        print(Name)
        
        Img = rows[2].find(class_="col-md-perfil").find("img").attrs["src"]
        Caps = []

        for cap in scrap.find_all("div",class_="capitulos"):
            Caps.append((cap.find("a").text.split("Cap. ")[1],cap.find("a").attrs["href"]))
        
        #descrição com a classe panel-body
        Desc = scrap.find(class_="panel-body").text

        # 0 = titulo alternativo
        # 1 = Generos
        # 2 = Autor
        # 3 = Artista
        # 4 = status
        MangaPerfil = scrap.find_all(class_="manga-perfil") 
        Genre = []
        for genre in MangaPerfil[1].find_all("a"):
            Genre.append(genre.text)

        manga = Manga(Name,path)
        manga.module = Union()
        manga.__ImgDownload__(Img)
        manga.Chapters = Caps
        manga.Desc = Desc
        manga.Genre = Genre
        manga.type = type
        manga.__UpdateObj__()
        pass