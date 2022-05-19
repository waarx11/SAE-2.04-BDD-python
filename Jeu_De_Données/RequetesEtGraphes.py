from curses import init_pair
import psycopg2 as psy
from getpass import getpass
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

def requeteSQL(): #Affichage des informations (Chaque Select est décrit dans le document: "Presentation")
# Connexion à la base
# Attention ! pensez à remplacer dblogin , login et mot_de_passe
# avec vos informations
        
        #n°1 Nombre total de champion dans le jeu qu'on peut utiliser
    print("Nombre total de champion dans le jeu :\n")
    df=pd.read_sql('''SELECT COUNT(*) FROM tChampion ;''', con=co)
    print(df)
    input()

        #n°2 On recupere les informations sur le champion 'Blitzcrank'
    print("Statistique du personnage Blitzcrank au niveau 1 :\n")
    df=pd.read_sql('''SELECT * FROM tCHAMPION WHERE nom='Blitzcrank' ;''', con=co)
    print(df)
    input()

        #n°3 Personnage ayant les dommages par coup le plus élevé (sans technique) le plus fort
    print("Personnage ayant les dommages par coup le plus élevé :\n")
    df=pd.read_sql('''SELECT nom , DommageAutoAtq FROM tChampion where DommageAutoAtq >= ALL (SELECT DommageAutoAtq FROM tChampion) ;''', con=co)
    print(df)
    input()

        #n°4 Les Personnages qui font plus de dégats Magique(sort) que de dégats physique(coup de poing, coup de pied...) 
    print("Listes des personnages qui font plus de dégats Magique(sort) que de dégats physique :\n")
    df=pd.read_sql('''SELECT nom FROM tChampion WHERE attaqueMagique>attaquePhysique ;''', con=co)
    print(df)
    input()

        #n°5 Personnage qui possède les meilleurs statistique global sur tout les attributs
    print("Personnage qui possède les meilleurs statistique global :\n")
    df=pd.read_sql('''SELECT *  
                        FROM tChampion 
                        WHERE ( attaquePhysique + defence + attaqueMagique + hP + mana + armure + resMagique + distanceAttaque + vitDp + vitAttaque + regenMana + regenHp + dommageAutoAtq + critique )
                        >= ALL (SELECT ( attaquePhysique + defence + attaqueMagique + hP + mana + armure + resMagique + distanceAttaque + vitDp + vitAttaque + regenMana + regenHp + dommageAutoAtq + critique ) FROM tchampion) ;''', con=co)
    print(df)
    input()

        #n°6 (Un champion est maximum niveau 18 et il commence au niveau 1) Celui qui possède le plus de point de vie à son niveau maximum sans item.
    print("Celui qui possède le plus de point de vie à son niveau maximum sans item :\n")
    df=pd.read_sql('''SELECT c.nom
                        FROM tChampion c, tLevelUp l
                        WHERE c.Cle=l.idChampion AND (c.hP+l.hp*17) >= ALL (Select (c.hP+l.hp*17) FROM tChampion c, tLevelUp l where c.Cle=l.idChampion) ;''', con=co)
    print(df)
    input()

        #n°7 Puissance de gnar au level 15
    print("Puissance du personnage 'Gnar' au niveau 15:")
    df=pd.read_sql('''SELECT nom, (c.DommageAutoAtq+l.DommageAutoAtq*14) as Degats_Lvl15
                        FROM tChampion c, tLevelUp l
                        WHERE nom='Gnar' and c.cle=l.idChampion;''', con=co)
    print(df)
    input()

        #n°8 Le ou Les Personnages qui ont le plus de dégat physique .
    print("Le ou Les Personnages qui ont le plus de dégat physique :")
    df=pd.read_sql('''SELECT nom, attaquePhysique Max_AtkPhys
                        FROM tChampion where attaquePhysique >= ALL (Select attaquePhysique from tChampion);''', con=co)
    print(df)
    input()

        #n°9 Nombre total dans le jeu
    print("Nombre total de botte existant :")
    df=pd.read_sql('''SELECT COUNT(*) as Nombre_de_botte
                        FROM titem
                        WHERE Nom LIKE '%Boots%';''', con=co)
    print(df)



def DiagrammeSQL():

    #Histogramme

    # Afficher un histogramme des personnage ayant une vitesse d'attaque < 1.5 / 1.5 <= x > 2.5 / >=2.5 au niveau 1.

    df = pd.read_sql(''' SELECT count(c.vitAttaque) 1.5, count(c1.vitAttaque) 1.5_2.5, count(c2.vitAttaque) 2.5
    #                      FROM tChampion c, tChampion c1, tChampion c2, 
    #                      WHERE c.vitAttaque < 1.5 AND c1.vitAttaque >= 1.5  AND c1.vitAttaque < 2.5 AND c2.vitAttaque  ''', con = co)
    df.plot(x="Personnage", y=['< 1.5', '1.5 <= x > 2.5', '>= 2.5'], legend = False, kind = 'bar')
    df.set_title('Diagramme Baton')
    df.set_xlabel('Personnage')
    df.set_ylabel('Type de capacité')
    plt.show()
    
    

    # Afficher un histogramme en fonction du libéllé de l'item.


def Camembert():

    #Camembert

    # Afficher en camembert le taux des différents Etiquettes(tank, support, ...).

    df = pd.read_sql(''' SELECT (SELECT count(type) 
                                    FROM tChampion 
                                    WHERE type Like '%Tank%') Tank,
		                    (SELECT count(type) 
                                    FROM tChampion 
                                    WHERE type Like '%Support%') Support,
                            (SELECT count(type) 
                                    FROM tChampion 
                                    WHERE type Like '%Mage%') Mage,
                            (SELECT count(type) 
                                    FROM tChampion 
                                    WHERE type Like '%Fighter%') Fighter,
                            (SELECT count(type)
                                    FROM tChampion 
                                    WHERE type Like '%Tireur%') Tireur,
                            (SELECT count(type) 
                                    FROM tChampion 
                                    WHERE type Like '%Assassin%') Assassin;''', con = co)
    df=df.transpose()
    fig= df.plot(y=0, kind='pie',labels=['Tank','Support','Mage','Fighters','Tireur','Assassin'],legend=True,autopct=lambda x: str(round(x,2))+ '%')
    fig.set_title('Classification des Rôles')
    plt.show()

    # Afficher en camembert le taux des différents types (mana / rage / rien).

    df = pd.read_sql(''' SELECT (SELECT count(*) 
		                         FROM tChampion 
		                         WHERE partype = 'Mana') Mana,
                                (SELECT count(*) 
                                 FROM tChampion 
                                 WHERE partype = 'Rage') Rage,
                                (SELECT count(*) 
                                 FROM tChampion 
                                 WHERE partype = 'Energy') Energie,
                                (SELECT count(*) 
                                 FROM tChampion 
                                 WHERE partype = 'Blood Well') Sang,
                               (SELECT count(*) 
                                 FROM tChampion 
                                 WHERE partype = 'None') as None
; ''', con = co)
    df=df.transpose()
    df.plot(y=0, kind='pie',labels=['Mana', 'Rage', 'Energie', 'Sang','None'],legend=True,autopct=lambda x: str(round(x,2))+ '%')
    plt.show()


    #Comparaison de camembert
    #On va montre le taux de champion ayant moin 450, le taux ayant entre 450 et 950, puis plus grand que 950, dans les différents niveau (3,10 et 18)
        #niveau 3
    df1 = pd.read_sql('''SELECT (SELECT COUNT(*) 
                            FROM tChampion c, tLevelUP l
                            WHERE c.cle = l.idChampion and ((c.mana)+l.mana*2)<450) ManaInférieur,
                            (SELECT COUNT(*) 
                            FROM tChampion c, tLevelUP l
                            WHERE c.cle = l.idChampion and ((c.mana)+l.mana*2)>=450 and ((c.mana)+l.mana*2)<=950) ManaMoyen,
                            (SELECT COUNT(*) 
                            FROM tChampion c, tLevelUP l
                            WHERE c.cle = l.idChampion and ((c.mana)+l.mana*2)>950) ManaSupérieur;
''', con=co)

    df2 = pd.read_sql('''SELECT (SELECT COUNT(*) 
                            FROM tChampion c, tLevelUP l
                            WHERE c.cle = l.idChampion and ((c.mana)+l.mana*6)<450) ManaInférieur,
                            (SELECT COUNT(*) 
                            FROM tChampion c, tLevelUP l
                            WHERE c.cle = l.idChampion and ((c.mana)+l.mana*6)>=450 and ((c.mana)+l.mana*2)<=950) ManaMoyen,
                            (SELECT COUNT(*) 
                            FROM tChampion c, tLevelUP l
                            WHERE c.cle = l.idChampion and ((c.mana)+l.mana*6)>950) ManaSupérieur;
''', con=co)

    df3 = pd.read_sql('''SELECT (SELECT COUNT(*) 
                            FROM tChampion c, tLevelUP l
                            WHERE c.cle = l.idChampion and ((c.mana)+l.mana*13)<450) ManaInférieur,
                            (SELECT COUNT(*) 
                            FROM tChampion c, tLevelUP l
                            WHERE c.cle = l.idChampion and ((c.mana)+l.mana*13)>=450 and ((c.mana)+l.mana*2)<=950) ManaMoyen,
                            (SELECT COUNT(*) 
                            FROM tChampion c, tLevelUP l
                            WHERE c.cle = l.idChampion and ((c.mana)+l.mana*13)>950) ManaSupérieur;
''', con=co)

    df4 = pd.read_sql('''SELECT (SELECT COUNT(*) 
                            FROM tChampion c, tLevelUP l
                            WHERE c.cle = l.idChampion and ((c.mana)+l.mana*17)<450) ManaInférieur,
                            (SELECT COUNT(*) 
                            FROM tChampion c, tLevelUP l
                            WHERE c.cle = l.idChampion and ((c.mana)+l.mana*17)>=450 and ((c.mana)+l.mana*2)<=950) ManaMoyen,
                            (SELECT COUNT(*) 
                            FROM tChampion c, tLevelUP l
                            WHERE c.cle = l.idChampion and ((c.mana)+l.mana*17)>950) ManaSupérieur;
''', con=co)


    figure, axes= plt.subplots(2,2)

    df1=df1.transpose()
    df1.plot(ax=axes[0][0],y=0, kind='pie',labels=['ManaInférieur','ManaMoyen','ManaSupérieur'],legend=True,autopct=lambda x: str(round(x,2))+ '%')
    axes[0][0].set_title("Stats mana pour les champion niveau 3")
    axes[0][0].set_ylabel('1') 

    df2=df2.transpose()
    df2.plot(ax=axes[0][1],y=0, kind='pie',labels=['ManaInférieur','ManaMoyen','ManaSupérieur'],legend=True,autopct=lambda x: str(round(x,2))+ '%')
    axes[0][1].set_title("Stats mana pour les champion niveau 7")
    axes[0][1].set_ylabel('2') 

    df3=df3.transpose()
    df3.plot(ax=axes[1][0],y=0, kind='pie',labels=['ManaInférieur','ManaMoyen','ManaSupérieur'],legend=True,autopct=lambda x: str(round(x,2))+ '%')
    axes[1][0].set_title("Stats mana pour les champion niveau 14")
    axes[1][0].set_ylabel('3')     

    df4=df4.transpose()
    df4.plot(ax=axes[1][1],y=0, kind='pie',labels=['ManaInférieur','ManaMoyen','ManaSupérieur'],legend=True,autopct=lambda x: str(round(x,2))+ '%')
    axes[1][1].set_title("Stats mana pour les champion niveau 18")  
    axes[1][1].set_ylabel('4')  

    plt.show()


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
    #requeteSQL()
    DiagrammeSQL()

    co.commit ()
    curs.close ()


# Affichage du message d'erreur en cas de problème de connexion
except (Exception , psy. DatabaseError ) as error :
    print ( error )
# Attention ! Toujours fermer la connexion lorsqu'on en a plus besoin
finally :
    if co is not None:
        co. close ()