
import io
from gtts import gTTS
import gtts
from playsound import playsound

r=io.open("malayalam.txt",mode="r",encoding="utf-8")
book_content=r.read()
ob=gTTS(book_content,lang="ml")
ob.save("malayalam.mp3")

playsound("malayalam.mp3")

