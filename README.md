# Machine-RAM
Création d'une Machine RAM dans le cadre de l'UE LSIN620 Modèles de Calcul & Complexité.

## Description
Ce projet a pour but l'implémentation d'une machine utilisant le langage **RAM**, version simplifiée et adaptée d'un [langage assembleur](https://fr.wikipedia.org/wiki/Assembleur). Un programme en langage RAM est composé d'une suite d'instructions et travaille sur un registre d'entrée donné.

## Le langage RAM
Le langage RAM utilisé contient le jeu d'instructions suivant :

| Instruction | Arguments | Desctiption |
| :- | :-: | :- |
| ADD | X, Y, R | Stocke le resultat de l'opération *X + Y* dans le registre R |
| DIV | X, Y, R | Stocke le resultat de l'opération *X / Y* dans le registre R |
| MULT | X, Y, R | Stocke le resultat de l'opération *X * Y* dans le registre R |
| JUMP | N | Saute *N* instructions |
| JL | X, Y, N | Saute *N* instructions si la valeur de X est strictement inférieure à la valeur de Y |
| JE | X, Y, N | Saute *N* instructions si les valeurs de X et Y sont égales |

<sub>*N, X et Y étant des entiers relatifs donnés directement ou des pointeurs de registres en contenant et R étant un pointeur de registre.*</sub>

## Utilisation / Spécifications techniques

Cette machine RAM utilise trois registres distincts :
 - Le registre d'entrée **i**  
Contenant l'entrée sur laquelle la machine travaillera et dont le premier élément i0 donne la taille.  
 - Le registre de travail **r**  
 Vide au démarrage, utilisé par la machine pour stocker temporairement des valeurs lors de l'exécution.  
 - Le registre de sortie **o**  
 Dans lequel le programme écrit et dont le contenu est retourné par la machine à la fin de l'exécution, et le premier élement o0 donne la taille.

Le programme à éxecuter doit être copié dans le fichier **input.1** précédé du registre d'entrée.

Ex :
```
3,20,19,42
ADD(0,1,O0)
ADD(I1,I2,R0)
JE(R0,I3,2)
ADD(R0,1,R0)
JUMP(-1)
ADD(0,R0,O1)
```

 <sub>D'autres exemples sont trouvables dans le dossier **Exemples_machines**.</sub>

 Une fois le fichier **input.1** rempli, l'exécution se fait via la commande ```make``` dans le terminal.


 À chaque changement d'état la configuration de la machine est affichée (Instruction, Étape, Contenu des registres).  

 Ex :
 ```
 ADD
 Etape: 4
 I ['I0 :3', 'I1 :20', 'I2 :19', 'I3 :42']
 T ['R0 :40']
 O ['O0 :1']
 ```

 Une fois l'exécution terminée, le registre de sortie est affiché.

 Ex:
 ```
 Sortie : ['O0 :1', 'O1 :42']
 ```

### Concernant le développement
Ce programme a été réalisé en utilisant Yacc et Lex pour la partie analyse syntaxique / analyse lexicale, ainsi que python pour la partie calcul et machine RAM.


### Collaborateurs
[DUPUY Raphael](https://www.linkedin.com/in/raphael-dupuy/) - [KANGA Elie](https://www.linkedin.com/in/elie-kanga/)

