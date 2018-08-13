#! python3

#cmd で mapit 住所


import webbrowser
import sys
import pyperclip

#address=input("住所を入力してください：")

if len(sys.argv)>1:
    address=sys.argv[1:]
    address=" ".join(address)
else:
    address=pyperclip.paste()

url="https://www.google.co.jp/maps/place/"+address
print(url)   
webbrowser.open(url)