import psycopg2 as psy
from getpass import getpass
import pandas as pd
from RequetesEtGraphes import *

def creationTab():  #Creation et Insertion des tables
    data=pd.read_csv(r'../Type_of_BDD/riot_champion.csv')
    data2=pd.read_csv(r'../Type_of_BDD/riot_item.csv')
    df1=pd.DataFrame(data)
    df12=df1.drop_duplicates()
    df2=pd.DataFrame(data2)
    df22=df2.drop_duplicates()

    #Drop tout les tables si elles existents
    curs.execute ('''DROP TABLE IF EXISTS tPossede ;''')
    curs.execute ('''DROP TABLE IF EXISTS tLevelUP ;''')
    curs.execute ('''DROP TABLE IF EXISTS tItem ;''')
    curs.execute ('''DROP TABLE IF EXISTS tSupp ;''')
    curs.execute ('''DROP TABLE IF EXISTS tChampion ;''')

    #Creation
    curs.execute ('''CREATE TABLE tChampion(
    cle CHAR(4) PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    type VARCHAR(50) NOT NULL,
    partype VARCHAR(30),
    attaquePhysique NUMERIC NOT NULL,
    defence NUMERIC NOT NULL,
    attaqueMagique NUMERIC,
    hP NUMERIC NOT NULL,
    mana NUMERIC,
    armure NUMERIC,
    resMagique NUMERIC,
    distanceAttaque NUMERIC,
    vitDp NUMERIC,
    vitAttaque NUMERIC,
    regenMana NUMERIC,
    regenHp NUMERIC,
    dommageAutoAtq NUMERIC,
    critique NUMERIC 
    );''')

    curs.execute ('''CREATE TABLE tLevelUP(
    idChampion CHAR(4) REFERENCES tChampion(cle),
    hP NUMERIC NOT NULL,
    mana NUMERIC,
    armure NUMERIC,
    resMagique NUMERIC,
    regenMana NUMERIC,
    regenHp NUMERIC,
    dommageAutoAtq NUMERIC,
    critique NUMERIC,
    PRIMARY KEY(idChampion)
    );''')

    curs.execute ('''CREATE TABLE tItem(
    iDItem CHAR(5) PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prixAchat NUMERIC NOT NULL,partytype tPossede(
    idChampion CHAR(4) REFERENCES tChampion(cle),
    idItem CHAR(5) REFERENCES tItem(iDItem)
    );''')

    #Insertion des données dans les tables
    for row in df12.itertuples():
        curs.execute('''INSERT INTO tChampion VALUES (%s ,%s ,%s , %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s);''',
                (row.key , row.name , row.tags, row.partype ,row.info_attack , row.info_defense , row.info_magic , row.stats_hp , row.stats_mp , row.stats_armor , row.stats_spellblock , row.stats_attackrange , row.stats_movespeed , row.stats_attackspeed , row.stats_mpregen , row.stats_hpregen , row.stats_attackdamage , row.stats_crit))
        curs.execute('''INSERT INTO tLevelUP VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s, %s);''',
                (row.key , row.stats_hpperlevel , row.stats_mpperlevel , row.stats_armorperlevel , row.stats_spellblockperlevel , row.stats_mpregenperlevel , row.stats_hpregenperlevel , row.stats_attackdamageperlevel , row.stats_critperlevel,)) 
    for row in df22.itertuples():
        curs.execute('''INSERT INTO tItem VALUES (%s ,%s ,%s ,%s ,%s);''',
                (row.item_id , row.name , row.buy_price , row.sell_price , row.explain))

    curs.execute('''UPDATE tLevelUP
                    SET critique = 10
                    WHERE idChampion IN (SELECT cle from tChampion WHERE type LIKE '%Fighter%'); ''')

    #Insertion dans la table tPossede en fonction du type du Champion et l'item qui le correspond
    curs.execute('''INSERT INTO tPossede SELECT cle, iDItem FROM tChampion, tItem i WHERE type LIKE '%Mage%' and i.nom = 'Boots of Speed' ;''')
    curs.execute('''INSERT INTO tPossede SELECT cle, iDItem FROM tChampion, tItem i WHERE type LIKE '%Tank%' and (i.nom = 'Abyssal Mask' or i.nom = 'Frozen Heart');''')
                   
    df=pd.read_sql('''SELECT * FROM tChampion ;''', con=co)
    print(df)



Choix = input("Comptez vous inserez les tables : (Oui ou Non)")

ident=input("Entrer votre identifiant :")

print ("Entrer votre mot de pass !")
password = getpass()

co = None
try:
# Connexion à la base
# Attention ! pensez à remplacer dblogin , login et mot_de_passe
# avec vos informations
    co = psy. connect (host='berlin',
            database ='db'+ident,
            user= ident,
            password = password)
    # Ajouter ici les interrogations de la base

    curs = co.cursor()

    if (Choix == "Oui"):
        creationTab()

    #requeteSQL()
    co.commit ()
    curs.close ()


# Affichage du message d'erreur en cas de problème de connexion
except (Exception , psy. DatabaseError ) as error :
    print ( error )
# Attention ! Toujours fermer la connexion lorsqu'on en a plus besoin
finally :
    if co is not None:
        co. close ()



























