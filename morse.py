#!/usr/bin/env python3
#-*- coding: utf-8 -*-

MORSECODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',

        '.': '.-.-.-', '+': '.-.-.', ',': '--..--',
        '_': '..--.-', ':': '---...', '$': '...-..-',
        '"': '.-..-.', '&': '.-...', '\'': '.----.',
        '/': '-..-.', '!': '-.-.--', '?': '..--..',
        '@': '.--.-.', '-': '-....-', ':': '-.-.-.',
        '(': '-.--.', ')': '-.--.-', '=': '-...-'
        }

def morseEncrypt(clearText):
    clearText = clearText.upper()
    cipherText = ""
    for s in clearText:
        if MORSECODE.__contains__(s):
            cipherText += MORSECODE[s] + ' '

    return cipherText

def morseDecrypt(cipherText):
    DEMORSECODE = {v:k for k,v in MORSECODE.items()}
    clearText = ""
    for s in cipherText.split(' '):
        if DEMORSECODE.__contains__(s):
            clearText += DEMORSECODE[s]

    return clearText.lower()

