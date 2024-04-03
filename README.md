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

<sub>*N, X et Y étant des entiers relatifs donnés directement ou des pointeurs de registres en contenant.*</sub>

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
JUMP(-2)
ADD(0,R0,O1)
```

 <sub>D'autres exemples sont trouvables dans le dossier **Exemples_machines**.</sub>

Une fois le fichier **input.1** rempli, l'exécution se fait via la commande ```make``` dans le terminal.



### Collaborateurs
[DUPUY Raphael](https://www.linkedin.com/in/raphael-dupuy/) - [KANGA Elie](https://www.linkedin.com/in/elie-kanga/)

