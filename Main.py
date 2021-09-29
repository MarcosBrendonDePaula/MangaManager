from Manga.Manga import Manga
from Modules.Neox import Neox

import os
print(os.getcwdb().decode("ascii"))
NM = Neox()
NM.__UpdateInfos__(manga_link="https://neoxscans.net/manga/solo-max-newbie/",path=os.getcwdb().decode("ascii"))
manga = Manga("Solo Max-Level Newbie ",path=os.getcwdb().decode("ascii"))
print(manga.GetCap(0).UnpackPages())
