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
<br>
Il faut savoir que notre jeu donnée comprend les 149 personnages du jeu et que celui-ci propose des caractériser les personnage par genre (ex : *Mage*, *Tank*, ...), mais nous avons aussi les caractéristique des personnages (ex : hp, distance d'attaque, attaque, armure, ...), nous aurons en plus l'augmentation des attributs de chaque personnage. <br>Ex: un personnage a 10 point de vie, en augmentent de niveau, ses points de vie augmente de 5.<br>
Aussi un jeu de donnée des items qu'on va devoir assimilé aux personnages.

<br>

## Objet

<br>

Notre jeu de donnée comprend les 248 items du jeu. Il faut savoir que certains item ont  

<br>

## *Idées-Requete*

<br>

1- Afficher le nombre de champion au total.<br>
2- Afficher l'identifiant "blitzcrank".<br>
3- Afficher le Champions qui fait le plus de dégats par coup (sans technique).<br>
4- Afficher les Champions qui possède plus de dégats magique que de dégats physique.<br>
5- Afficher le Champions qui possède les meilleurs stats(somme de tout les stats).<br>
6- Afficher le personnages avec le plus d'hp au niveau maximum, sans item.<br>
7- Combien d'attaque aurais gnar si on l'augmente du niveau 3 au niveau 15.<br>
8- Affiche celui qui a le plus de dégat physique .<br>
9- Combien d'item "botte" y t'il dans la liste d'item.<br>
10- Diagramme par la moyenne des prix de vente des items par libelle.<br>



- Afficher un histogramme des personnage ayant une vitesse d'attaque < 1.5 / 1.5 <= x > 2.5 / >=2.5 au niveau 1.
- Afficher un histogramme en fonction du libéllé de l'item.


- Afficher en camembert le taux des différents Etiquettes(tank, support, ...) .
- Afficher en camembert le taux des différents types (mana / rage / rien).

- Afficher un diagramme baton en fonction du prix des item.

Comparaison de camembert :
- Afficher 3 camembert :
     - niv 3 : Mana < 450 et Mana > 950
     - niv 7 :  Mana < 450 et Mana > 950
     - niv 14 :  Mana < 450 et Mana > 950
     - niv 18 : Mana < 450 et Mana > 950


## MCD

<img src="MCD.png"
     alt="MCD"
     style="float: left; margin-right: 40px;" />

<br>

## MLD

<img src="MLD.png"
     alt="MLD"
     style="float: left; margin-right: 40px;" />

<br>

## Description des diagrammes

### Diagramme circulaire
Nous allons commencer par la description des diagramme circulaire.



<img src="Role.png"
     alt="Role"
     style="float: left; margin-right: 40px;" />


Dans ce diagramme, nous faisons une étude sur les charactéristique des champions. En effet, nous voulons savoir le pourcentage de chaque role de personnage qui sont présent dans le jeux. Il y a plusieurs, nous avons des Mage, Support, Tank, Assissin et les Fighteur. Comme nous pouvons le voir ci dessus, nous avons une majorité de fighters avec 27.47% des champions, suivi de près par les mages 24.89% des champions. Puis enfin, nous avoir 18.45% de tank, 15.45% d'assassin et 13.73% support

Pour être plus précis, nous avons 64 fighters, 58 mages, 43 tanks, 36 assassins et 32 supports. Il faut aussi savoir qu'un champion peut avoir plusieurs role ce qui expliquer que l'addition de tout les roles donne un nombre supérieur au nombre total de champion qui est de 148.


<br>

<img src="TypeChamp.png"
     alt="TypeChamp"
     style="float: left; margin-right: 40px;" />
     
Ce diagramme nous permet de connaitre en pourcentage ce que consomme chaque champion pour le combat. Le type mana est sans aucun doute le type le plus utiliser du jeux avec ces 85.14% de champions qui s'en sert. Vient ensuite le type energie qui est lui utiliser a hauteur de 5.41%. 

Il reste donc le type rage et sang utiliser respectivement a hauteur de 4.73% et 1.35%. Pour finir il y a également des personnages qui n'utilise pas d'energie et ces dernier représente 3.38% des champions du jeux.

<br>



<img src="Compare.png"
     alt="Compare"
     style="float: left; margin-right: 40px;" />

Passons maintenant au chose sérieux, nous allons faire une études de l'évolution de mana max de l'ensemble des champions en fonction de leurs niveau. En effet, a chaque niveau, les champions upgrade de leurs mana max.

Nous allons commencé par le niveau 3 puis 7 puis 14 et enfin 18. Nous allons chercher le pourcentage de champion ayant moins de 450 de mana max, puis entre 450 et 950 et enfin plus de 950 mana.

Comme nous pouvons le voir, pour les champions de niveau 3, à peu près ou les team fight commencent. Plus de 70% des champions ont moins de 450 de mana, moins de 30% des champions ont entre 450 et 950 de mana. Alors qu'aucun champion n'a encore plus de 950 de mana.2cm

Nous arrivons aux champions de niveau 7. On constate qu'aucun n'a encore dépassé le seuil des 950 mana max, alors qu'on peut voir une net augmentation des champions de plus de 50% passant de moins de 450 de mana à l'intervalle [450, 950] de mana.

Ensuite nous lorsque les champions passe le niveau 14, nous pouvons constaté que nous passons enfin le seuil des 0% pour les champions ayant plus de 950 mana max. Environ 13.5% des champions sont dans cette catégorie. Le passage dans cette catégorie explique la légère diminution des 2 autres seuils.

Enfin, lorsque les champions passe le niveau 18, on peut voir que le nombre de champions ayant plus de 950 mana max a presque triplé. alors que les champions ayant moins de 450 de mana sont presque ceux, qui ne consomme pas le type mana.

Pour conclure cette étude, comme nous avons pu le voir dans précedente requete, une majorité du jeu consomme de la mana, ce qui expliqu'au niveau maximum (18), une grande majorité soient vers les + 950 et sur l'intervalle [450, 950].


<br>


### Diagramme bâton


<br>

<img src="Change.png"
     alt="Change"
     style="float: left; margin-right: 40px;" />

<br>

<img src="Change.png"
     alt="Change"
     style="float: left; margin-right: 40px;" />

<br>

<img src="Change.png"
     alt="Change"
     style="float: left; margin-right: 40px;" />

<br>

<img src="Change.png"
     alt="Change"
     style="float: left; margin-right: 40px;" />
<br>

### Courbe


<br>

<img src="Change.png"
     alt="Change"
     style="float: left; margin-right: 40px;" />

<br>

<img src="Change.png"
     alt="Change"
     style="float: left; margin-right: 40px;" />

<br>

<img src="Change.png"
     alt="Change"
     style="float: left; margin-right: 40px;" />

<br>

<img src="Change.png"
     alt="Change"
     style="float: left; margin-right: 40px;" />

<br>