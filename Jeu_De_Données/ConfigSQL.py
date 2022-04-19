import psycopg2 as psy
from getpass import getpass
import pandas as pd
import psycopg2 as psy

def creationTab():
    data=pd.read_csv(r'../Type_of_BDD/riot_champion.csv')
    data2=pd.read_csv(r'../Type_of_BDD/riot_item.csv')
    df1=pd.DataFrame(data)
    df12=df1.drop_duplicates()
    df2=pd.DataFrame(data2)
    df22=df2.drop_duplicates()
    curs.execute ('''DROP TABLE IF EXISTS tChampion ;''')
    curs.execute ('''DROP TABLE IF EXISTS tLevelUP ;''')
    curs.execute ('''DROP TABLE IF EXISTS tItem ;''')
    curs.execute ('''DROP TABLE IF EXISTS tPossede ;''')
    curs.execute ('''DROP TABLE IF EXISTS tSupp ;''')

    curs.execute ('''CREATE TABLE tChampion(
    cle CHAR(4) PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
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

    # curs.execute ('''CREATE TABLE tLevelUP(
    # idChampion CHAR(4) REFERENCES tChampion(cle),
    # hP NUMERIC NOT NULL,
    # mana NUMERIC,
    # armure NUMERIC,
    # resMagique NUMERIC,
    # regenMana NUMERIC,
    # regenHp NUMERIC,
    # dommageAutoAtq NUMERIC,
    # critique NUMERIC,
    # PRIMARY KEY(idChampion)
    # );''')

    # curs.execute ('''CREATE TABLE tItem(
    # iDItem CHAR(5) PRIMARY KEY,
    # nom VARCHAR(50) NOT NULL,
    # prixAchat NUMERIC NOT NULL,
    # prixVente NUMERIC NOT NULL,
    # libelle VARCHAR(200) NOT NULL
    # );''')

    # curs.execute ('''CREATE TABLE tPossede(
    # idChampion CHAR(4) REFERENCES tChampion(cle),
    # seperieur CHAR(5) REFERENCES tItem(iDItem)
    # );''')

    # curs.execute ('''CREATE TABLE tSupp(
    # idItem CHAR(5) REFERENCES tItem(iDItem)
    # seperieur CHAR(5) REFERENCES tItem(iDItem)
    # );''')

    for row in df12.itertuples():
        curs.execute('''INSERT INTO tChampion VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s);''',
                (row.key , row.name , row.info.attack , row.info.defense , row.info.magic , row.stats.hp , row.stats.mp , row.stats.armor , row.stats.spellblock , row.stats.attackrange , row.stats.movespeed , row.stats.attackspeed , row.stats.mpregen , row.stats.hpregen , row.stats.attackdamage , row.stats.crit))
    #     curs.execute('''INSERT INTO tLevelUP VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s);''',
    #             (row.key , row.stats.hpperlevel , row.stats.mpperlevel , row.stats.armorperlevel , row.stats.spellblockperlevel , row.stats.mpregenperlevel , row.stats.hpregenperlevel , row.stats.attackdamageperlevel , row.stats.critperlevel)) 
    # for row in df22.itertuples():
    #     curs.execute('''INSERT INTO tItem VALUES (%s ,%s ,%s ,%s ,%s);''',
    #             (row.item_id , row.name , row.buy_price , row.sell_price , row.explain))
    # res = curs.fetchone ()#prend une ligne de mon curs
    # while res is not None:# temps qu'il y a des éléments / lignes dans le fetchone
    #     print (res)
    #     res = curs.fetchone ()
    df=pd.read_sql('''SELECT COUNT(*) FROM tChampion ;''', con=co)
    print(df)


# def requeteSQL():

#     df=pd.read_sql('''SELECT COUNT(*) FROM tChampion ;''', con=co)
#     print(df)

#     df=pd.read_sql('''SELECT * FROM CHAMPION WHERE ID='Blitz' ;''', con=co)
#     print(df)

#     df=pd.read_sql('''SELECT MAX(Dégat) FROM tChampion ;''', con=co)
#     print(df)

#     df=pd.read_sql('''SELECT MAX(Dégat) FROM tChampion ;''', con=co)
#     print(df)

#     df=pd.read_sql('''SELECT MAX(Dégat) FROM tChampion ;''', con=co)
#     print(df)


ident=input("Entrer votre identifiant :")

print ("Entrer votre mot de pass !")
password = getpass()

co = None
try:
    # Connexion à la base
# Attention ! pensez à remplacer dblogin , login et mot_de_passe
#avec vos informations
    co = psy. connect (host='berlin',
            database ='db'+ident,
            user= ident,
            password = password)
    # Ajouter ici les interrogations de la base

    curs = co.cursor()
    
    creationTab()
    # requeteSQL()

    co.commit ()
    curs.close ()


# Affichage du message d'erreur en cas de problème de connexion
except (Exception , psy. DatabaseError ) as error :
    print ( error )
# Attention ! Toujours fermer la connexion lorsqu'on en a plus besoin
finally :
    if co is not None:
        co. close ()



























