#!/usr/bin/env python3
#-*- coding: utf-8 -*-

BACONCODE = {'a': 'AAAAA', 'b': 'AAAAB', 'c': 'AAABA', 'd': 'AAABB',
             'e': 'AABAA', 'f': 'AABAB', 'g': 'AABBA', 'h': 'AABBB',
             'i': 'ABAAA', 'j': 'ABAAA-', 'k': 'ABAAB', 'l': 'ABABA',
             'm': 'ABABB', 'n': 'ABBAA', 'o': 'ABBAB', 'p': 'ABBBA', 
             'q': 'ABBBB', 'r': 'BAAAA', 's': 'BAAAB', 't': 'BAABA', 
             'u': 'BAABB', 'v': 'BAABB-', 'w': 'BABAA', 'x': 'BABAB', 
             'y': 'BABBA', 'z': 'BABBB'}

BACONCODE_SEC = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb',
                 'E': 'aabaa', 'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 
                 'I': 'abaaa', 'J': 'abaab', 'K': 'ababa', 'L': 'ababb',
                 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba', 'P': 'abbbb',
                 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
                 'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb',
                 'Y': 'bbaaa', 'Z': 'bbaab'}

def baconEncrypt(clearText):
    clearText = clearText.upper() 
    cipherText = ""
    for s in clearText:
        if BACONCODE_SEC.__contains__(s):
            cipherText += str(BACONCODE_SEC[s])

    return cipherText.upper()

def baconDecrypt(cipherText):
    DEBACONCODE_SEC = {v:k for k,v in BACONCODE_SEC.items()}
    cipherText = list(cipherText.lower())
    clearText = ""

    for i in range(0,len(cipherText)):
        if cipherText[i]!='a' and cipherText[i]!='b':
            cipherText[i] = ''
    cipherText = ''.join(cipherText)
            
    i = 0
    while(i+5 <= len(cipherText)):
        code = str(cipherText[i:i+5])
        if DEBACONCODE_SEC.__contains__(code):
           clearText += DEBACONCODE_SEC[code]
        i += 5
    
    return clearText

