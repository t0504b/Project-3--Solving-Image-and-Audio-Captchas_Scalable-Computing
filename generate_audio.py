#pip install gTTS
from gtts import gTTS 
import os
import random

with open('symbols.txt', 'r') as file:
    symbols = file.read().replace('\n', '')

for j in range(20000):
  s = ''
  for i in range(8):
    s = s + str(symbols[random.randint(0,len(symbols)-1)])
  mytext = s
  language = 'en'
  myobj = gTTS(text=mytext, lang=language, slow=False) 
  myobj.save("audio_captchas/"+s+".mp3")
  if j % 300 == 0:
    print(str(j)+' done')

