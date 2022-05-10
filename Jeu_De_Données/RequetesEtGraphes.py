import pandas as pd
import psycopg2 as psy

def requeteSQL(): #Affichage des informations (Chaque Select est décrit dans le document: "Presentation")

    # n°1
    df=pd.read_sql('''SELECT COUNT(*) FROM tChampion ;''', con=co)
    print(df)

        # n°2
    df=pd.read_sql('''SELECT * FROM CHAMPION WHERE ID='Blitz' ;''', con=co)
    print(df)

        # n°3
    df=pd.read_sql('''SELECT * FROM tChampion Having Max(DommageAutoAtq) ;''', con=co)
    print(df)

        #n°4
    df=pd.read_sql('''SELECT * FROM tChampion WHERE attaquePhysique>attaqueMagique ;''', con=co)
    print(df)

        #n°5
    df=pd.read_sql('''SELECT * as Meilleurs_Stats 
                        FROM tChampion 
                        WHERE ( attaquePhysique + defence + attaqueMagique + hP + mana + armure + resMagique + distanceAttaque + vitDp + vitAttaque + regenMana + regenHp + dommageAutoAtq + critique )
                        >= (SELECT ( attaquePhysique + defence + attaqueMagique + hP + mana + armure + resMagique + distanceAttaque + vitDp + vitAttaque + regenMana + regenHp + dommageAutoAtq + critique ) FROM tchampion) ;''', con=co)
    print(df)

        #n°6 (Un champion est maximum niveau 18 et il commence au niveau 1)
    df=pd.read_sql('''SELECT * 
                        FROM tChampion c, LevelUp l
                        WHERE c.Cle=l.idChampion AND (c.hP+l.hp*17) >= (Select (c.hP+l.hp*17) FROM tChampion c, LevelUp l where c.Cle=l.idChampion) ;''', con=co)
    print(df)

        #n°7 
    df=pd.read_sql('''SELECT nom, (c.DommageAutoAtq+l.DommageAutoAtq*14) as Degats_Lvl15
                        FROM tChampion c, LevelUp l
                        WHERE nom='gnar' ;''', con=co)
    print(df)

        #n°8
    df=pd.read_sql('''SELECT nom, max(attaquePhysique) Max_AtkPhys
                        FROM tChampion c ;''', con=co)
    print(df)

        #n°9
    df=pd.read_sql('''SELECT nom, max((c.attaquePhysique + l.attaquePhysique*17)) As Max_AtkPhys_Niv18
                        FROM tChampion c, LevelUp l
                        WHERE c.Cle=l.idChampion;''', con=co)
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

    #Camembert

    #Diagramme en baton

    #Diagramme

    #Comparaison de camembert

