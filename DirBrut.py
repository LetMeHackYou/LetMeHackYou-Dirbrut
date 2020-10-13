import socket
import requests
import os
text = []
print(os.system("figlet DirBrut"))
url = input("enter the Url:")
def connection(url):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if "http://" in url:
        new_url = url.replace("http://", "")
    elif "https://" in url:
        new_url = url.replace("https://", "")
    s.connect((new_url,80))
    while True:
        print("the host is alive")
        break
connection(url)
print("please select the wordlist size:\n")
print("1.Small\n2.Medium\n3.Big\n4.Custom\n")
list = int(input(""))
if list == 1:
    wordlist = open("/usr/share/wordlists/dirb/small.txt", "r")
    dir = wordlist.read()
    text = dir.split()
elif list == 2:
    wordlist = open("/usr/share/wordlists/dirb/common.txt","r")
    dir = wordlist.read()
    text = dir.split()
elif list == 3:
    wordlist = open("/usr/share/wordlists/dirbuster/directory-list-1.0.txt","r")
    dir = wordlist.read()
    text = dir.split()
elif list == 4:
    wordlist = input("Enter the directory of the Custom Wordlist:")
    word = open(wordlist)
    dir = word.read()
    text = dir.split()
else:
    print("invalid input")
for i in range(len(text)):
    r = requests.get(url+"/"+str(text[i]))
    if r.status_code == 200:
        print(url+"/"+text[i])
        os.system("touch dir.txt")
        log = open("dir.txt")
        t = log.write(url+"/"+text[i])