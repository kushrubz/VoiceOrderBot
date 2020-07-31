import speech_recognition as sr
import pyttsx3 as p
import array as arr
from PROJECTS.Jarvis.Beverage import select_Beverages
#from PROJECTS.Jarvis.Starters import *
#from PROJECTS.Jarvis.Mains import *
options = ['Beverages','Starters','Mains']
r1 = sr.Recognizer()

engine = p.init()
engine.say('Helllo I am Edith')
engine.say('Welcome to Wok Singh Chinese Restaurant')
engine.say('How are you today?')
engine.runAndWait()

with sr.Microphone() as source:
    r1.adjust_for_ambient_noise(source)
    print('How are you?')
    audio = r1.listen(source)

    try:
        text = r1.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError:
        print("")

engine.say("What would you like to have")
engine.runAndWait()
print(options)



#giving instructions/Placing orders
def get_instructions():
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        r2.adjust_for_ambient_noise(source)
        print("Choose one")
        audio = r2.listen(source)


        try:
            instruction = r2.recognize_google(audio)
            print(instruction)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError:
            print("")
    return instruction


instruction1 = get_instructions()

if "beverage" in instruction1:
    bot = select_Beverages()
    Beverage1=bot.get_category()
    print(Beverage1)
#elif "Starters" in instruction:
 #   bot = Starters()
#elif "Mains" in instruction:
 #   bot = Mains()
#else:
 #   engine.say('invalid input')





