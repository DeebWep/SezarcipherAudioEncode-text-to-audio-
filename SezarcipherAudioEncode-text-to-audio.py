from gtts import gTTS
import os
import cv2
import numpy as np
ciphercharsen_A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphercharsen_a = "abcdefghijklmnopqrstuvwxyz"
badchars = " "
text = input("Enter Text: ")
key = int(input("Enter Key Number: "))
textready = []
cipher_text = ""
for i in text:
    textready.append(i)

for j in textready:
    if j.isalpha():
        if j.isupper():
            k = ciphercharsen_A.index(j)
            k+=key
            if k >=26:
                k=k%26
            cipher_text += ciphercharsen_A[k]
        if j.islower():
            k = ciphercharsen_a.index(j)
            k+=key
            if k>=26:
                k=k%26
            cipher_text +=ciphercharsen_a[k]
    else:
        cipher_text += j
#print("Cipher Text: ",cipher_text)

dil = input("Enter the abbreviation of the language you want to encrypt If you don't know the abbreviations, type X and wait: ")
dillerr = ['en','fr','zh-CN','zh-TW','pt','es','tr']
while dil=='X' or dil not in dillerr:
    resim=cv2.imread('diller.png')
    cv2.imshow('gTTS Languages:',resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    dil = input("Enter the abbreviation of the language you want to encrypt If you don't know the abbreviations, type X and wait: ")

tts = gTTS(text=cipher_text,lang=dil,slow=True,)
document_name = input("What name do you want to save your file under?: ")+'.mp3'
tts.save(document_name)
os.system(document_name)
