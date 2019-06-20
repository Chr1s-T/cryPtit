#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def benchEncrypt(clearText, benches):
    l = 0
    cipherText = ""
    clearText = list(clearText)
    groups = int(benches)
    if len(clearText)<=benches:
        return clearText
    
    charList = [clearText[i:i+groups] for i in range(0,len(clearText),groups)]

    try:
        while(len(charList[l]) > 0):
            char = charList[l].pop(0)
            cipherText +=  char
            l = (l+1)%len(charList)
            if(len(charList[-1]) == 0):
                charList.pop()
    except:
        return cipherText

    return cipherText

def benchDecrypt(cipherText, benches=0):
    clearText = []
    cipherText = list(cipherText)

    if(benches):
        if(len(cipherText)%benches == 0):
            clearText = [benches, benchEncrypt(cipherText, len(cipherText)/benches)]
        else:
            clearText = [benches, benchEncrypt(cipherText, int(len(cipherText)/benches)+1)]
        return clearText
    
    for bench in range(2, len(cipherText)):
        if(len(cipherText)%bench == 0):
            clearText.append([bench, benchEncrypt(cipherText, len(cipherText)/bench)])

    if len(clearText) == 0:
        clearText = [[1, ''.join(cipherText)]]
        return clearText

    return clearText

