from gtts import gTTS
from playsound import playsound

n=input("ENTER A NUMBER:")
token="ടോക്കൺ നമ്പർ"+n
obj=gTTS(token,lang="ml")
obj.save("token.mp3")

playsound("token.mp3")

