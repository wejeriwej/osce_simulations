import os

import sounddevice as sd
import soundfile as sf


import speech_recognition as sr

end_the_while = 0
while end_the_while != 1:
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

    
        

#start of the IF statements
    #if Sentence.__contains__("name") and Sentence.__contains__("age"):
            

    if Sentence.__contains__("name") and Sentence.__contains__("age"):
        print("im zak and im 24")
    elif Sentence.__contains__("name") or Sentence.__contains__("call"):
        data, fs = sf.read('My name is zak.wav', dtype='float32')
        sd.play(data, fs)
        status = sd.wait()

    elif Sentence.__contains__("age") or Sentence.__contains__("old"):
        data, fs = sf.read('age.wav', dtype='float32')
        sd.play(data, fs)
        status = sd.wait()

    elif Sentence.__contains__("Sorry, I couldn't understand, could you repeat what you said"):
        print("Sorry, I couldn't understand, could you repeat what you said")
            

    elif Sentence.__contains__("stop") or Sentence.__contains__("end") or Sentence.__contains__("consultation"):
        print("End of consultation")
        end_the_while +=1

    else:
        print ("Sorry, Not sure")             

