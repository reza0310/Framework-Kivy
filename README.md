# Framework-Kivy
Juste un peu de code pour faciliter une utilisation poussée du module Kivy de Python

# Documentation
<br><br>
## framework.TextInput(x, y, tx, ty, placeholder, password=False, source="textinput")

### Description:
Les entrées textuelles de Kivy ayant des problèmes de type changer la couleur des trucs environnants avec mon framework, j'ai décidé de les refaire.

### Entrées:
x -> Coordonnée verticale de l'entrée dans le plan 1000x1000.<br>
y -> Coordonnée horizontale de l'entrée dans le plan 1000x1000.<br>
tx -> Taille verticale de l'entrée dans le plan 1000x1000.<br>
ty -> Taille horizontale de l'entrée dans le plan 1000x1000.<br>
placeholder -> Le texte qui s'affiche quand l'entrée est vide.<br>
password -> Booléenne permettant de savoir si il faut afficher le texte ou des * à la place.<br>
source -> clef du dictionnaire globals.images permettant savoir quelle image afficher en fond.

### Sortie:
Une instance d'un objet qui affiche à globals.FPS images par seconde votre entrée textuelle. Utilisez instance.remove() pour le supprimer.

<br><br>
## globals.hud.bind((x, y), (tx, ty), action)

### Description:
Méthode permettant de créer un bouton.

### Entrées:
x -> Coordonnée verticale de l'entrée dans le plan 1000x1000.<br>
y -> Coordonnée horizontale de l'entrée dans le plan 1000x1000.<br>
tx -> Taille verticale de l'entrée dans le plan 1000x1000.<br>
ty -> Taille horizontale de l'entrée dans le plan 1000x1000.<br>
action -> Le code à exécuter quand le bouton est appuyé (Je recommande fortement d'utiliser un appel à une méthode sans arguments et en prennant en compte le fait qu'elle sera exécutée depuis le script framework).

### Sortie:
Un bouton, invisible mais quand vous appuyez au bon endroit ça fait l'action.

<br><br>
## globals.hud.unbind(unbin="all")

### Description:
Méthode permettant de détruire un ou plusieurs bouton(s).

### Entrées:
unbin -> L'action du/des bouton(s) à supprimer. "all" est un cas spécial qui détruit tout les boutons.

### Sortie:
Ba le bouton y'a pu d'bouton.

<br><br>
## globals.hud.texte(x, y, texte, remove=True, color=(1, 1, 1, 1), taille_police=30)

### Description:
Méthode permettant d'afficher du texte.

### Entrées:
x -> Coordonnée verticale de l'entrée dans le plan 1000x1000.<br>
y -> Coordonnée horizontale de l'entrée dans le plan 1000x1000.<br>
texte -> Le texte à afficher.<br>
remove -> Si c'est sur True, le texte ne restera que pour une frame. Si c'est sur false, vous devrez exécuter framework.layout.canvas.remove(instance) pour le supprimer.<br>
color -> Tuple RGBA indiquant la couleur.<br>
taille_police -> La taille de la police d'écriture.

### Sortie:
Un tuple contenant en position 0 l'instance et en position 1 un False.

<br><br>
## globals.hud.image(x, y, tx, ty, image, remove=True)

### Description:
Méthode permettant d'afficher une image.

### Entrées:
x -> Coordonnée verticale de l'entrée dans le plan 1000x1000.<br>
y -> Coordonnée horizontale de l'entrée dans le plan 1000x1000.<br>
tx -> Taille verticale de l'entrée dans le plan 1000x1000.<br>
ty -> Taille horizontale de l'entrée dans le plan 1000x1000.<br>
image -> Le path de votre image. Je recommande d'utiliser la variable ultra-globale globals.images pour ça.<br>
remove -> Si c'est sur True, le texte ne restera que pour une frame. Si c'est sur false, vous devrez exécuter framework.layout.canvas.remove(instance) pour le supprimer.

### Sortie:
Un tuple contenant en position 0 l'instance et en position 1 un False.
