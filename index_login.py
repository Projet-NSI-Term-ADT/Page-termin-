# -*- coding: utf-8 -*-
#import sys
#sys.stdout.reconfigure(encoding='utf-8')
from fonction import *
import cgi

formulaire = cgi.FieldStorage()
email = formulaire.getvalue('email')
username = formulaire.getvalue('username')
password = formulaire.getvalue('password')
date = formulaire.getvalue('date')

uname = formulaire.getvalue('uname')
mdp = formulaire.getvalue('mdp')


html2 = "<p> Cet identifiant ou cet email est déjà utilisé </p>"

html3 ="<p> tu es connecté connard</p>"

html4 ="<p> Mot de passe ou identifiant incorrect  </p>"



#sing_in_unique


file = open('index_login.html', "r", encoding="utf-8")

f = file.read()

if uname == None and username == None:
    print(f)

if email != None and username != None and password != None and date != None:
    sign = sign_in_unique(username, password , email , date)
    if sign == False:
        print(f.replace("<!---%html2%-->", html2 ))
    else:
        file = open('index_jeu.html', "r", encoding="utf-8")
        f = file.read()
        print(f)


if uname != None and mdp != None : 
    log = login(uname, mdp)
    if log == True:
        file2 = open('index_jeu.html', "r", encoding="utf-8")
        f2 = file2.read()
        print(f2)
    else:
        print(f.replace(" <!---%html3%-->", html4 ))

    
print("</body> </html>")


file.close()

