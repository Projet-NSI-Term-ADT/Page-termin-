import sqlite3
bdd = sqlite3.connect("BASE_DONNEES_SITE.db")
curseur = bdd.cursor()


def sign_in(identifiant, mdp , ad_mail , date_naissance):
    requete = "INSERT INTO UTILISATEURS (Identifiant, Mdp, Adresse_mail, Date_de_naissance) VALUES (?, ?, ?, ?);"
    curseur.execute(requete, (identifiant, mdp , ad_mail , date_naissance))
    bdd.commit()
    requete = f"SELECT Identifiant FROM UTILISATEURS WHERE Identifiant = '{identifiant}' OR Adresse_mail = '{ad_mail}'"
    curseur.execute(requete)
    test = curseur.fetchall()
    if test == [] :
        return False
    return True

def sign_in_unique(identifiant, mdp , ad_mail , date_naissance):
    requete = f"SELECT Identifiant FROM UTILISATEURS WHERE Identifiant = '{identifiant}' OR Adresse_mail = '{ad_mail}'"
    curseur.execute(requete)
    test = curseur.fetchall()
    if test == [] :
        res=sign_in(identifiant, mdp , ad_mail , date_naissance)
        return res
    return False


def login(identifiant, mdp):
    requete = f"SELECT Identifiant , Mdp FROM UTILISATEURS WHERE Identifiant = '{identifiant}' AND Mdp = '{mdp}'"
    curseur.execute(requete)
    test = curseur.fetchall()
    if test != [] :
        return True
    return False
 



def demande_dev(identifiant,fiche_profil):
    requete = f"INSERT INTO DEV (Nom, Profil) VALUES (?, ?);"
    curseur.execute(requete,(identifiant,fiche_profil))
    

def valider_dev(identifiant):
    requete = f"UPDATE UTILISATEURS SET Validation_dev = 1 WHERE Identifiant = '{identifiant}'"
    curseur.execute(requete)

def retirer_dev(identifiant):
    requete = f"UPDATE UTILISATEURS SET Validation_dev = 0 WHERE Identifiant = '{identifiant}'"
    curseur.execute(requete)
    

