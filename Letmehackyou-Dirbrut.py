import requests
import sys
url = input("enter the url")
if sys.platform == "darwin":
    wordlist = input("enter the directory of the wordlist:")
elif sys.platform == "linux2":
    res = requests.get("url")
    if res.status_code == 200:
        print("select the size of the wordlist..\n")
        print("1.Small\n2.Medium\n3.Big\n4.custom")
        opt = input("")
        if opt == 1:
            wordlist = open("/usr/share/wordlists/dirb/small.txt","r")
        elif opt == 2:
            wordlist = open("/usr/share/wordlits/dirb/normal.txt","r")
        elif opt == 3:
            wordlist = open("/usr/share/wordlists/dirb/big.txt","r")
        elif opt == 4:
            wordlist = input("enter the directory:")
        else:
            print("invalid input")
    else:
        print("host is not working")
for dir in wordlist:
    brut = requests.get("url"+"/"+dir)
    if brut.status_code == 200:
        print("url"+"/"+dir)
