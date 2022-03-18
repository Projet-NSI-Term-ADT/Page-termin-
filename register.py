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




html2 = f"""
                    <p> Cet identifiant ou cet email est déjà utilisé </p>
                  """

html3 = f"""
                    <p> mauvais mdp </p>
                  """


html4 = f"""
                    <p> tu es connecté connard</p>
                  """
#sing_in_unique


file = open('index_login.html', "r", encoding="utf-8")

f = file.read()
    

if email != None and username != None and password != None and date != None:
    sign = sign_in_unique(username, password , email , date)
    if sign == False:
        print(f.replace("%html2%", html2 ))
    else:
        print(f) #a remplacer par la destination


if uname != None and mdp != None :
    log = login(uname, mdp)
    if log == True:
        print(f.replace("%html3%", html3 ))
    else:
        print(f.replace("%html3%", html4 )) #a remplacer par la destination
    
print("</body> </html>")


