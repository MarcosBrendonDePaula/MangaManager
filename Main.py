from Manga.Manga import Manga
from Modules.Neox import Neox

import os
print(os.getcwdb().decode("ascii"))
NM = Neox()
NM.__UpdateInfo__(manga_link="https://neoxscans.net/manga/dragon-ego",type="Manga")
manga = Manga("Dragon Ego ",path=os.getcwdb().decode("ascii"))
manga.__CapDownload__(10)
print(manga.GetCap(10).UnpackPages())