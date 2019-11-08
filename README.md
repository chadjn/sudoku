# Sudoku

## Utilisation du Sudoku
À ce jour, le Sudoku ne possède ni interface graphique, ni timer et n'automatise pas l'effacement des brouillons. Cependant, il est tout à fait opérationnel. Il ne propose également que trois niveaux (une grille par niveau).
Toutes les informations dont vous aurez besoin pour interagir avec le sudoku vous seront expliquées au fur et à mesure du jeu. Amusez-vous bien !

## Initialisation du git (pour Lucille et Léa)
* Ouvrir ton terminal.
* Parcourir tes fichiers jusqu'à accéder à l'endroit où tu veux ranger tout le projet (ex: C:\Users\Charlotte\Documents\Master MCN\Projets\Semestre 7\Sudoku) --> voir le tutoriel sur le terminal sur OpenClassRoom
* Copier-coller l'instruction `git clone https://github.com/chadjn/sudoku.git` et appuyer sur la touche "Entrée" de ton clavier
* Copier-coller et compléter l'instruction `git checkout [ton prénom]` (ex: `git checkout Charlotte`) et appuyer sur la touche "Entrée" de ton clavier
* Copier-coller l'instruction `git add *` et appuyer sur la touche "Entrée" de ton clavier

### Vérification de votre initialisation
* Créer un script que tu appelleras [ton prénom].py (ex: Charlotte.py) qui aura pour seule instruction `print("Hello world!")`.
* Copier-coller (et compléter si nécessaire) les instructions suivantes dans ton terminal :
    * `git add [ton prénom].py`
    * `git commit -m "Mon premier commit : trop fière de moi !"`
    * `git push`
    
## Commandes pour git
À chaque fois que tu retravailleras sur le projet, il faudra suivre ces instructions.
### Récupérer les données
Dès que tu ouvres le projet et avant chaque fois que tu veux pousser du contenu sur git :
`git fetch origin`

### Envoyer des données
Dans l'ordre, à chaque fois que tu veux envoyer du contenu :
- `git add` + le nom du fichier à ajouter (pour chaque nouveau fichier créé)
- `git commit -m "` +  le message du commit + `"`
- `git push`