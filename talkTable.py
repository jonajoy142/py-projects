
import pyttsx3  #this will work 


dec={1:"ones",
    2:"twos",
    3:"threes",
    4:"fours",
    5:"fives",
    6:"sixes",
    7:"sevens",
    8:"eights",
    9:"nines",
    10:"tens",


    }
speaker=pyttsx3.init()
def multiplication(num):
    for i in range(1,11):
        ans=i*num
        txt=str(i)+" "+dec[num]+" "+"are"+" "+str(ans)
        print(txt)
        speaker.say(txt)
        speaker.runAndWait()
        
    speaker.say("thankyou")
    speaker.runAndWait()

n=int(input("ENTER A NUMBER:"))
multiplication(n)



