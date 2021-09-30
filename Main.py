from Manga.Manga import Manga
from Modules.UnionMangas import Union
from Modules.Neox import Neox

import os

NM = Neox()
UM = Union()


UM.__UpdateInfo__(manga_link="https://unionmangas.top/pagina-manga/a-noiva-do-predador",type="Manga")
manga = Manga("a noiva do predador",path=os.getcwdb().decode("ascii"))
manga.__CapDownload__(1)
print(manga.GetCap(1).UnpackPages())