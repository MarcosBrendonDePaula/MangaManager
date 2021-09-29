from Manga.Manga import Manga
from Modules.Neox import Neox

import os
print(os.getcwdb().decode("ascii"))
neoxModule = Neox()
#neoxModule.__UpdateInfos__(manga_link="https://neoxscans.net/manga/a-sensitive-issue",path=os.getcwdb().decode("ascii"))
#novo = Manga("Teste1",path=os.getcwdb().decode("ascii"))
#cap = novo.GetCap(2)
manga = Manga("A Sensitive Issue ",path=os.getcwdb().decode("ascii"))
print(manga.GetCap(0).UnpackPages())