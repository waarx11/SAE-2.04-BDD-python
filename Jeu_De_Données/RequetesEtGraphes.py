import pandas as pd
import psycopg2 as psy
import matplotlib.pyplot as plt
from sympy import false

co = None

def requeteSQL(): #Affichage des informations (Chaque Select est décrit dans le document: "Presentation")

        #n°1 Nombre total de champion dans le jeu qu'on peut utiliser
    df=pd.read_sql('''SELECT COUNT(*) FROM tChampion ;''', con=co)
    print(df)

        #n°2 On recupere les informations sur le champion 'Blitzcrank'
    df=pd.read_sql('''SELECT * FROM tCHAMPION WHERE nom='Blitzcrank' ;''', con=co)
    print(df)

        #n°3 Personnage ayant les dommages par coup (sans technique) le plus fort
    df=pd.read_sql('''SELECT * FROM tChampion where DommageAutoAtq >= ALL (SELECT DommageAutoAtq FROM tChampion) ;''', con=co)
    print(df)

        #n°4 Les Personnages qui font plus de dégats Magique(sort) que de dégats physique(coup de poing, coup de pied...) 
    df=pd.read_sql('''SELECT * FROM tChampion WHERE attaqueMagique>attaqueAttaque ;''', con=co)
    print(df)

        #n°5 Personnage qui possède les meilleurs statistique global sur tout les attributs
    df=pd.read_sql('''SELECT *  
                        FROM tChampion 
                        WHERE ( attaquePhysique + defence + attaqueMagique + hP + mana + armure + resMagique + distanceAttaque + vitDp + vitAttaque + regenMana + regenHp + dommageAutoAtq + critique )
                        >= ALL (SELECT ( attaquePhysique + defence + attaqueMagique + hP + mana + armure + resMagique + distanceAttaque + vitDp + vitAttaque + regenMana + regenHp + dommageAutoAtq + critique ) FROM tchampion) ;''', con=co)
    print(df)

        #n°6 (Un champion est maximum niveau 18 et il commence au niveau 1) Celuiqui possède le plus de point de vie à son niveau maximum sans item
    df=pd.read_sql('''SELECT c.nom
                        FROM tChampion c, tLevelUp l
                        WHERE c.Cle=l.idChampion AND (c.hP+l.hp*17) >= ALL (Select (c.hP+l.hp*17) FROM tChampion c, tLevelUp l where c.Cle=l.idChampion) ;''', con=co)
    print(df)

        #n°7 Puissance de gnar au level 15
    df=pd.read_sql('''SELECT nom, (c.DommageAutoAtq+l.DommageAutoAtq*14) as Degats_Lvl15
                        FROM tChampion c, tLevelUp l
                        WHERE nom='Gnar' and c.cle=l.idChampion;''', con=co)
    print(df)

        #n°8 Les Personnages qui ont le plus de dégat physique au niv 1
    df=pd.read_sql('''SELECT nom, attaquePhysique Max_AtkPhys
                        FROM tChampion where attaquePhysique >= ALL (Select attaquePhysique from tChampion);''', con=co)
    print(df)

        #n°9
    df=pd.read_sql('''SELECT nom, (c.attaquePhysique + l.attaqueAuto*17) As Max_AtkPhys_Niv18
                         FROM tChampion c, tLevelUp l
                         WHERE c.Cle=l.idChampion AND (c.attaquePhysique + l.attaquePhysique*17) >= ALL (SELECT (c.attaquePhysique + l.attaquePhysique*17) FROM tChampion c, tLevelUp l WHERE c.Cle=l.idChampion);''', con=co)
    print(df)

        #n°10
    df=pd.read_sql('''SELECT nom, (c.DommageAutoAtq+l.DommageAutoAtq*14) as Degats_Lvl15
                        FROM tChampion c, LevelUp l
                        WHERE (c.hp+l.hp*14)>1500
                        GROUP BY (c.hp+l.hp*14)
                        ORDER BY DESC;''', con=co)
    print(df)

        #n°11
    # df=pd.read_sql('''SELECT nom, (c.DommageAutoAtq+l.DommageAutoAtq*14) as Degats_Lvl15
    #                     FROM tChampion c, LevelUp l
    #                     WHERE (c.hp+l.hp*14)>1500
    #                     GROUP BY (c.hp+l.hp*14);''', con=co)
    # print(df)

        #n°12
    df=pd.read_sql('''SELECT COUNT(*) as Nombre_de_botte
                        FROM item
                        WHERE Nom LIKE "%Boots%";''', con=co)
    print(df)



# def DiagrammeSQL():

    #Histogramme

    # Afficher un histogramme des personnage ayant une vitesse d'attaque < 1.5 / 1.5 <= x > 2.5 / >=2.5 au niveau 1.

    

    # Afficher un histogramme en fonction du libéllé de l'item.

    #Camembert

    # Afficher en camembert le taux des différents Etiquettes(tank, support, ...).

    df = pd.read_sql(''' SELECT count(c.type) Tank, count(c1.type) Support, count(c2.type) Mage, count(c3.type) Fighter, count(c4.type) Tireur, count(c5.type) Assassin
                         FROM tChampion c, c1, c2, c3, c4, c5
                         WHERE c.type Like '%Tank%' AND c1.type Like '%Support%' AND c2.type Like '%Mage%' AND c3.type Like '%Fighter%' AND c4.type = '%Marksman%' AND c5.type Like '%Assassin%' ''', con = co)
    df.plot(x="Personnage", y=['Tank', 'Support', 'Mage', 'Fighter', 'Tireur', 'Assassin'], legend = False, kind = 'bar')
    df.set_title('Diagramme Baton')
    df.set_xlabel('Personnage')
    df.set_ylabel('Type de capacité')
    plt.show()
    df = pd.read_sql()

    # Afficher en camembert le taux des différents types (mana / rage / rien).

    df = pd.read_sql(''' SELECT count(c.partype) Mana, count(c1.partype) Rage, count(c2.partype) Energie, count(c3.partype) Sang, count(c4.partype) null,
                         FROM tChampion c, c1, c2, c3, c4
                         WHERE c.partype = 'Mana' AND c1.partype = 'Rage' AND c2.partype = 'Energy' AND c3.partype LIKE 'Blood %' AND c4.partype = 'None' ''', con = co)
    df.plot(x="Personnage", y=['mana', 'rage', 'energie', 'blood', 'null'], legend = False, kind = 'bar')
    df.set_title('Diagramme Baton')
    df.set_xlabel('Personnage')
    df.set_ylabel('Type de capacité')
    plt.show()
    df = pd.read_sql()

    #Diagramme en baton

    #Comparaison de camembert


# requeteSQL()