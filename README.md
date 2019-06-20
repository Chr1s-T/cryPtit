### CryPtit: An easy way to encrypt/decrypt the password in CTF game

#### Usage：

Usage: cryPtit.py -o <original strings> -<d|e> --<bench|caesar|bacon|morse> [-r]         

**Options:**
  -h, --help            show this help message and exit                                  
  -o ORIGSTR, --original=ORIGSTR
                        the original strings to be encryptd or decryptd                  
  -r ROTATE, --rotate=ROTATE
                        specify the rotate if you used BenchEncrypt or                   
                        CaesarEncrypt
  -d, --decrypt         decrypt the string you input                                     
  -e, --encrypt         encrypt the string you input                                     
  --bench               encrypt/decrypt the string using bench                           
  --bacon               encrypt/decrypt the string using bacon                           
  --caesar              encrypt/decrypt the string using caesar                          
  --morse               encrypt/decrypt the string using morse 

#### Example：

```bash
#bacon decrypt:
./cryPtit.py -d --bacon -o BABAAABBABAAABBAABAAAABABABAAAABBABAABAAAAABBUNDEFINEDBABAAABBABAAABBAABAAAABABABAAAABBABAABAAAAABB

#caesar/rot13 decrypt:
./cryPtit.py -e --caesar -r 13 -o "nopq"

#morse, default input/output is splitting with a space,change it to "/" if you want it with your technique
./cryPtit.py -e --morse  -o "morse"
./cryPtit.py -d --morse  -o "-- --- .-. ... ."

#bench decrypt:
./cryPtit.py -d --bench -o "TEESCPEHRIAIHR" -r 2
./cryPtit.py -d --bench -o "TEESCPEHRIAIHR"
```

#### Development:

The script is still waiting to be greater and greater, hope for your comments and requirements.

