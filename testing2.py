from gtts import gTTS
import os
from pygame import mixer
mixer.init()
from time import ctime
import time

import speech_recognition as sr

counter_for_while = '0' #this is for the while loop that determines the name of the .mp3 file
end_the_while = 0
while end_the_while != 1:

    while counter_for_while != '100':

        
        r = sr.Recognizer()
        with sr.Microphone() as source:
                
            r.adjust_for_ambient_noise(source)
            print("Say something...")
            audio = r.listen(source)
            try:
                Sentence1 = r.recognize_google(audio)
                Sentence = Sentence1.lower()
                print("You have said: \n"+Sentence)
                    
            except Exception as e:
                #print("I could not undertand.\nError : " + str(e))
                Sentence = "Sorry, I couldn't understand, could you repeat what you said"

    #Is code for speech        
        def speak(audioString):
            print(audioString)    
                
            tts = gTTS(text=audioString, lang='en')
            tts.save("audio" + counter_for_while + ".mp3")
            os.system("mpg321"+"audio" + counter_for_while + ".mp3")

            
        def speak_out():
            mixer.music.load("audio" + counter_for_while + ".mp3")
            mixer.music.play()
        

    #start of the IF statements
        if Sentence.__contains__("name") and Sentence.__contains__("age"):
            speak ("My name is Zak and I'm 24")
            speak_out()
            time.sleep(2)
            counter_for_while +='1'

        elif Sentence.__contains__("name") or Sentence.__contains__("call"):
            speak ("My name is Zak")
            speak_out()
            time.sleep(2)
            counter_for_while +='1'

        elif Sentence.__contains__("age") or Sentence.__contains__("old"):
            speak ("I'm 24")
            speak_out()
            time.sleep(2)
            counter_for_while +='1'

        elif Sentence.__contains__("Sorry, I couldn't understand, could you repeat what you said"):
            speak ("Sorry, I couldn't understand, could you repeat what you said")
            speak_out()
            time.sleep(5)
            counter_for_while +='1'

        elif Sentence.__contains__("stop") or Sentence.__contains__("end"):
            speak("End of consultation")
            speak_out()
            time.sleep(2)
            counter_for_while = '100'
            end_the_while +=1

        else:
            speak ("Sorry, Not sure")
            speak_out()
            time.sleep(2)              

