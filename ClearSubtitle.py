#Author : D4Vinci
#Clear subtitles files from coloring codes so if you wanted to play movies on tv without any annonying codes
#Usage : ClearSubtitle.py <Subtitle_file>

import sys,re
srt = sys.argv[1]
codes = ["</font>","<i>","</i>"]
font_regex = re.compile(r".font color=.#[a-z|A-Z|0-9]*..") #"""<font color="#FFA500">"""
font_regex2 = re.compile(r".font color=#[a-z|A-Z|0-9]*.")  #"""<font color=#FFA500>"""
ra5ama_regex = re.compile(r"{.*}") #"""{\fs50\fad(1000,1500)\c&#008008&\..\...\..\....}"""
f=open(srt,"r")
subtitles=f.read()
f.close()
extracted=font_regex.findall(subtitles)
extracted+=font_regex2.findall(subtitles)
extracted+=ra5ama_regex.findall(subtitles)
all = extracted + codes
for i in all :
      subtitles=subtitles.replace(i,"")

open(srt,"w").write(subtitles)
