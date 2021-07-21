# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 12:42:29 2021

@author: Lenovo
"""
#speech recgnizer can only recnize .wav file only 


#libary for speech
import speech_recognition as sr
#audio file path and variable
Audio_file=("a.wav")
#use the audio file as source


r=sr.Recognizer()
with sr.AudioFile(Audio_file) as source:
    audio=r.record(source)
    
try:
    print("Audio file contain "+r.recognize_google(audio))
except sr.UnknownValueError:
    print(" sorry:-audio cannot recognize file ")
except sr.RequestError:
    print("google cannot get the result from google speech")
