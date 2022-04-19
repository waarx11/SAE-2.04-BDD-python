---
title: "SAE 2.04"
author: VERDIER Nathan, KARTAL Emre, MUZARD Thomas
geometry: margin=2cm
---

# Présentation du jeu de donnée

Dans le cadre de  notre SAE 2.04 : Exploitation d'une base de donnée, nous avons choisie de traiter un jeu de donnée sur le thème de Leagues of Legend. C'est un jeu pc qui reprendra l'ensemble des personnages du jeu ainsi que ses items.
Lien de notre bases de données [LOL-Champions and Item](https://www.kaggle.com/datasets/gyejr95/league-of-legendslol-champion-and-item-2020).

<br>

## Personnages

Il faut savoir que notre jeu donnée comprend les 149 personnages du jeu. Il faut savoir que celui-ci propose des caractériser les personnage pas genre (ex : *Mage*, *Tank*, ...), mais nous avons aussi les caractéristique des personnages (ex : hp, distance d'attaque, attaque, armure, ...).

<br>

## Objet

Notre jeu de donnée comprend les 248 items du jeu. Il faut savoir que certains item ont  

## Idées-Requete

1- Afficher le nombre de champion au total
2- Afficher l'identifiant "blitzcrank"
3- Afficher le Champions qui fait le plus de dégats.
4- Afficher les Champions les plus faciles à jouer
5- Afficher les Champions les plus forts à jouer
6- Afficher les Champions qui possède plus de dégats magique que de dégats physique
7- Afficher les Champions qui possède les meilleurs stats(somme de tout les stats)
8- Combien d'attaque aurais gnar si on l'augmente du niveau 3 au niveau 15
9- Affiche celui qui a le plus de dégat physique au niv 1
10- Afficher celui qui a le plus de dégat physique au niveau 18
11- Afficher par ordre décroissant, les champions ayant leurs hp > 1500 au niveau 15
12- Afficher les items superieur que peut faire la "digger"
13- Combien d'item "botte" y t'il dans la liste d'item.



- Afficher un histogramme des personnage ayant une vitesse d'attaque < 1.5 / 1.5 <= x > 2.5 / >=2.5 au niveau 1
- Afficher un histogramme en fonction du libéllé de l'item


- Afficher en camembert le taux des différents Etiquettes(tank, support, ...) 
- Afficher en camembert le taux des différents types (mana / rage / rien).

- Afficher un diagramme baton en fonction du prix des item
- Afficher un diagramme des item qui ont ou pas besoin d'autres item pour etre craft

Comparaison de camembert :
- Afficher 3 camembert :
     - niv 3 : Mana < 450 et Mana > 950
     - niv 10 :  Mana < 450 et Mana > 950
     - niv 18 : Mana < 450 et Mana > 950


## MCD

<img src="MCD.png"
     alt="MCD"
     style="float: left; margin-right: 40px;" />

<br>


```mermaid
graph TD;
     POSSEDE-->CHAMPION;

     POSSEDE-->ITEMS;
     SUPERIEUR-->ITEMS;
     SUPERIEUR-->ITEMS;

```
