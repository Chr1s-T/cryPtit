#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import bacon
import bench
import caesar
import morse
import optparse
import sys

def main():
    parser = optparse.OptionParser("%prog "+\
           "-o <original strings> -<d|e> --<bench|caesar|bacon|morse> [-r]" )

    parser.add_option('-o','--original',dest='origStr',type='string', \
           help="the original strings to be encryptd or decryptd" )
    parser.add_option('-r','--rotate', dest='rotate',type='int', \
           help="specify the rotate if you used BenchEncrypt or CaesarEncrypt" )
    parser.add_option('-d','--decrypt',dest='decrypter',action="store_true", \
           default=False, help='decrypt the string you input')
    parser.add_option('-e','--encrypt',dest='encrypter',action="store_true", \
           default=False, help='encrypt the string you input')

    parser.add_option('--bench',dest='bench',action="store_true", \
           default=False, help='encrypt/decrypt the string using bench')
    parser.add_option('--bacon',dest='bacon',action="store_true", \
           default=False, help='encrypt/decrypt the string using bacon')
    parser.add_option('--caesar', dest='caesar', action="store_true", \
           default=False, help='encrypt/decrypt the string using caesar')
    parser.add_option('--morse', dest='morse', action="store_true", \
           default=False, help='encrypt/decrypt the string using morse')

    (options, args) = parser.parse_args()
    origStr = options.origStr
    decrypter = options.decrypter
    encrypter = options.encrypter
    _bench = options.bench
    _bacon = options.bacon
    _caesar = options.caesar
    _morse = options.morse
    rotate = options.rotate

    if (origStr==None):
        print('Nothing to be encrypted/decrypted.')
        exit(False)
    if (decrypter==False and encrypter==False):
        print('Encrypt or decrypt? It\'s a question?')
    if (_bench==False and _bacon==False and _caesar==False and _morse==False):
        print('Please specify a method to encode or decode it.')

    if(encrypter==True):
        if(_bench==True):
            if(rotate == None):
                exit("Rotate argument is required.")
            rst = bench.benchEncrypt(origStr, rotate)
            print("Bench Encrypt:\n" + rst)

        elif(_caesar==True):
            if(rotate==None):
                exit("Rotate argument is required.")
            rst = caesar.caesarEncrypt(origStr, rotate)
            print("Caesar Encrypt:\n" + rst)

        elif(_bacon==True):
            rst = bacon.baconEncrypt(origStr)
            print("Bacon Encrypt:\n" + rst)

        elif(_morse==True):
            rst = morse.morseEncrypt(origStr)
            print("Morse Encrypt:\n" + rst)

    if(decrypter==True):
        if(_bench==True):
            if(rotate):
                rst = bench.benchDecrypt(origStr, rotate)
                print("Column %d: %s" %(rst[0], rst[1]))
            else:
                rst = bench.benchDecrypt(origStr)
                for r in rst:
                    print("Column %d: %s" %(r[0], r[1]))

        elif(_caesar==True):
            if(rotate):
                rst = caesar.caesarDecrypt(origStr, rotate)
                print("Rotate by %d: %s" % (rotate, rst))
            else:
                for i in range(0, 26):
                    rst = caesar.caesarDecrypt(origStr, i+1)
                    print("Rotate by %d: %s" % (i+1, rst))

        elif(_bacon==True):
            rst = bacon.baconDecrypt(origStr)
            print("Bacon Decrypt:\n" + rst)

        elif(_morse==True):
            rst = morse.morseDecrypt(origStr)
            print("Morse Decrypt:\n" + rst)

if __name__ == '__main__':
     main()
