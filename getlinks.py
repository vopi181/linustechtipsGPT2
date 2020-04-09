#!/usr/bin/env python

import requests
import subprocess
from bs4 import BeautifulSoup

src = requests.get("https://www.youtube.com/user/LinusTechTips/videos").text
soup = BeautifulSoup(src, 'html.parser')
video_els = soup.find_all("a")
video_els = list(filter(lambda x: "watch" in x.attrs["href"], video_els))
def rip_link(ele):
    return("https://youtube.com"+ele.attrs["href"])

for i, el in enumerate(video_els):
    link = rip_link(el)
    print(f"[{i}] Doing {link}")
    subprocess.call(f"source getyoutubecaptions.sh; cap {link} > captions/{i}.txt", shell=True)
    

