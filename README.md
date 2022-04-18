# Framework-Kivy
Juste un peu de code pour faciliter une utilisation poussée du module Kivy de Python

# Documentation

## framework.TextInput(x, y, tx, ty, placeholder, password=False, source="textinput")

### Description:
Les entrées textuelles de Kivy ayant des problèmes de type changer la couleur des trucs environnants avec mon framework, j'ai décidé de les refaire.

### Entrées:
x -> Coordonnée verticale de l'entrée dans le plan 1000x1000.
y -> Coordonnée horizontale de l'entrée dans le plan 1000x1000.
tx -> Taille verticale de l'entrée dans le plan 1000x1000.
ty -> Taille horizontale de l'entrée dans le plan 1000x1000.
placeholder -> Le texte qui s'affiche quand l'entrée est vide.
password -> Booléenne permettant de savoir si il faut afficher le texte ou des * à la place.
source -> clef du dictionnaire globals.images permettant savoir quelle image afficher en fond.

### Sortie:
Une instance d'un objet qui affiche à globals.FPS images par seconde votre entrée textuelle. Utilisez instance.remove() pour le supprimer.


## globals.hud.bind((x, y), (tx, ty), action)

### Description:
Méthode permettant de créer un bouton.

### Entrées:
x -> Coordonnée verticale de l'entrée dans le plan 1000x1000.
y -> Coordonnée horizontale de l'entrée dans le plan 1000x1000.
tx -> Taille verticale de l'entrée dans le plan 1000x1000.
ty -> Taille horizontale de l'entrée dans le plan 1000x1000.
action -> Le code à exécuter quand le bouton est appuyé (Je recommande fortement d'utiliser un appel à une méthode sans arguments et en prennant en compte le fait qu'elle sera exécutée depuis le script framework).

### Sortie:
Un bouton, invisible mais quand vous appuyez au bon endroit ça fait l'action.


## globals.hud.unbind(unbin="all")

### Description:
Méthode permettant de détruire un ou plusieurs bouton(s).

### Entrées:
unbin -> L'action du/des bouton(s) à supprimer. "all" est un cas spécial qui détruit tout les boutons.

### Sortie:
Ba le bouton y'a pu d'bouton.


## globals.hud.texte(x, y, texte, remove=True, color=(1, 1, 1, 1), taille_police=30)

### Description:
Méthode permettant d'afficher du texte.

### Entrées:
x -> Coordonnée verticale de l'entrée dans le plan 1000x1000.
y -> Coordonnée horizontale de l'entrée dans le plan 1000x1000.
texte -> Le texte à afficher.
remove -> Si c'est sur True, le texte ne restera que pour une frame. Si c'est sur false, vous devrez exécuter framework.layout.canvas.remove(instance) pour le supprimer.
color -> Tuple RGBA indiquant la couleur.
taille_police -> La taille de la police d'écriture.

### Sortie:
Un tuple contenant en position 0 l'instance et en position 1 un False.


## globals.hud.image(x, y, tx, ty, image, remove=True)

### Description:
Méthode permettant d'afficher une image.

### Entrées:
x -> Coordonnée verticale de l'entrée dans le plan 1000x1000.
y -> Coordonnée horizontale de l'entrée dans le plan 1000x1000.
tx -> Taille verticale de l'entrée dans le plan 1000x1000.
ty -> Taille horizontale de l'entrée dans le plan 1000x1000.
image -> Le path de votre image. Je recommande d'utiliser la variable ultra-globale globals.images pour ça.
remove -> Si c'est sur True, le texte ne restera que pour une frame. Si c'est sur false, vous devrez exécuter framework.layout.canvas.remove(instance) pour le supprimer.

### Sortie:
Un tuple contenant en position 0 l'instance et en position 1 un False.
