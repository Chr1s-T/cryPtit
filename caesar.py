#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def caesarEncrypt(clearText, rotate):
    cipherText = ""
    for char in clearText:
        if char>='a' and char<='z':
            asc = (ord(char)+rotate-ord('a'))%26 + ord('a')
            cipherText += chr(asc)
        elif char>='A' and char<='Z':
            asc = (ord(char)+rotate-ord('A'))%26 + ord('A')
            cipherText += chr(asc)
        else:
            cipherText += char

    return cipherText

def caesarDecrypt(cipherText, rotate):
    clearText = ""
    for char in cipherText:
        if char>='a' and char<='z':
            asc = (ord(char)-rotate-ord('a'))%26 + ord('a')
            clearText += chr(asc)
        elif char>='A' and char<='Z':
            asc = (ord(char)-rotate-ord('A'))%26 + ord('A')
            clearText += chr(asc)
        else:
            clearText += char

    return clearText

