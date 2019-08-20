import speech_recognition as sr
import serial
import time
ser1 = serial.Serial('COM6', 9600)
r = sr.Recognizer()
keywords = ['thank', 'hello', 'watch', 'speak']  
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone..")
    r.adjust_for_ambient_noise(source, duration=5)
    print("Listening...")
    for i in range(1, 10):
        audio = r.listen(source, timeout=2.5)
        try:
            string = r.recognize_google(audio)
            list_speech = string.split()
            for i in range(len(list_speech)):
                if list_speech[i] in keywords:
                    print("Keywords found '" + list_speech[i] + "'")
                    if (list_speech[i] == 'thank'):
                        ser1.write('1'.encode())
                    if (list_speech[i] == 'hello'):
                        ser1.write('2'.encode())
                    if (list_speech[i] == 'watch'):
                        ser1.write('3'.encode())
                    if (list_speech[i] == 'speak'):
                        ser1.write('4'.encode())
        except sr.UnknownValueError:
            print("Audio couldn't be understood")
        except sr.RequestError as e:
            print("Google error; {0}".format(e))
'''
for more information check out this video:
https://www.youtube.com/watch?v=E2ybPWA99JU&t=77s
'''
            
        
    

