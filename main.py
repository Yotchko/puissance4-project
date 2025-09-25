
# ETAPE 1
# Définition des dimensions de la grille
ROWS = 6  # Nombre de lignes
COLS = 7  # Nombre de colonnes

# ca c'est la fonction pour créer une grille vide 6x7
def create_grid():
    # On utilise une liste de listes pour représenter les cases
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

# la ta la fonction pour afficher la grille dans la console
def print_grid(grid):
    for row in grid:
        # c'est pour afficher chaque ligne avec des | entre les cases ... bref ta capté
        print("|".join(row))
    # Ligne de séparation en bas de la grille
    print("-" * (2 * COLS - 1))

# Point d'entrée du programme
if __name__ == "__main__":
    # Création de la grille
    grid = create_grid()
    # Affichage de la grille
    print_grid(grid)


# ETAPE 2
# Fonction pour insérer un jeton ('X' ou 'O') dans une colonne
# D'abord le jeton doit tommber dans la premiere case vide en partqnt du bas
def insert_token(grid, col, token):
    """
    Insère un jeton dans la colonne spécifiée.
    Retourne True si l’insertion a réussi, False si la colonne est pleine.
    """
    # On parcourt les lignes de bas en haut
    for row in reversed(range(ROWS)):
        if grid[row][col] == " ":
            grid[row][col] = token  # Place le jeton dans la première case vide
            return True
    return False  # Colonne pleine, insertion impossible

# Exemple d'utilisation
# On insère un jeton X dans la colonne 3
insert_token(grid, 3, "X")
print("\nAprès insertion d'un jeton X dans la colonne 3 :")
print_grid(grid)



# ETAPE 3
# Fonction pour vérifier une victoire horizontale pour un Joueur.
def check_horizontal_win(grid, token):
    """
    Vérifie si le joueur avec le jeton donné a 4 jetons consécutifs horizontalement.
    Retourne True si victoire, False sinon.
    """
    for row in grid:
        count = 0  # compteur de jetons consécutifs
        for cell in row:
            if cell == token:
                count += 1
                if count == 4:
                    return True  # victoire trouvée
            else:
                count = 0  # reset si cellule différente
    return False  # aucune victoire horizontale

#ETAPE 3 - 2eme partie  
#En gros c'est pour tester si je loeur X a gagné en créant une ligne horizontale de 4 jetons 
# et apres il affiche la grille avec le résultat de la victoire. 
# Exemple : test de victoire horizontale
insert_token(grid, 0, "X")
insert_token(grid, 1, "X")
insert_token(grid, 2, "X")
insert_token(grid, 3, "X")

print("\nGrille après insertion pour test victoire horizontale :")
print_grid(grid)
print("Victoire horizontale X :", check_horizontal_win(grid, "X"))



# ETAPE 4 - partie 1
# Exemple : test de victoire verticale
grid = create_grid()  # On repart d'une grille vide
insert_token(grid, 2, "O")
insert_token(grid, 2, "O")
insert_token(grid, 2, "O")
insert_token(grid, 2, "O")

print("\nGrille après insertion pour test victoire verticale :")
print_grid(grid)
print("Victoire verticale O :", check_vertical_win(grid, "O"))


# ETAPE 4 partie 2
# Exemple : test de victoire verticale
grid = create_grid()  # On repart d'une grille vide
insert_token(grid, 2, "O")
insert_token(grid, 2, "O")
insert_token(grid, 2, "O")
insert_token(grid, 2, "O")

print("\nGrille après insertion pour test victoire verticale :")
print_grid(grid)
print("Victoire verticale O :", check_vertical_win(grid, "O"))


#ETAPE 5 partie 1
# Vérifie si un joueur a 4 jetons alignés en diagonale
def check_diagonal_win(grid, token):
    # Vérifie les diagonales  (haut-gauche → bas-droit)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (grid[row][col] == token and
                grid[row + 1][col + 1] == token and
                grid[row + 2][col + 2] == token and
                grid[row + 3][col + 3] == token):
                return True

    # Vérifie les diagonales  (bas-gauche → haut-droit)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if (grid[row][col] == token and
                grid[row - 1][col + 1] == token and
                grid[row - 2][col + 2] == token and
                grid[row - 3][col + 3] == token):
                return True

    return False

# ETAPE 5 partie 2

# Exemple : test de victoire diagonale
grid = create_grid()  # Grille vide

# Créer une diagonale ↘️ avec des "X"
insert_token(grid, 0, "X")
insert_token(grid, 1, "O")  # jeton de l'autre joueur pour "caler"
insert_token(grid, 1, "X")
insert_token(grid, 2, "O")
insert_token(grid, 2, "O")
insert_token(grid, 2, "X")
insert_token(grid, 3, "O")
insert_token(grid, 3, "O")
insert_token(grid, 3, "O")
insert_token(grid, 3, "X")

print("\nGrille après insertion pour test victoire diagonale :")
print_grid(grid)
print("Victoire diagonale X :", check_diagonal_win(grid, "X"))



# ETAPE 6 partie 1

# Vérifie si un joueur a gagné (horizontal, vertical ou diagonal)
def check_win(grid, token):
    return (check_horizontal_win(grid, token) or
            check_vertical_win(grid, token) or
            check_diagonal_win(grid, token))

#Etape 6 partie 2
# Exemple : test de victoire avec check_win globale
grid = create_grid()

# Créer une ligne horizontale pour X
insert_token(grid, 0, "X")
insert_token(grid, 1, "X")
insert_token(grid, 2, "X")
insert_token(grid, 3, "X")

print("\nTest check_win globale :")
print_grid(grid)
print("Victoire X :", check_win(grid, "X"))


# ETAPE 7 
# Lance une partie avec deux joueurs (X et O) qui jouent chacun leur tour
def play_game():
    grid = create_grid()
    game_over = False
    current_player = "X"  # Le joueur X commence

    while not game_over:
        print_grid(grid)
        print(f"\nTour du joueur {current_player}")

        # Choix de la colonne (saisi par le joueur)
        col = int(input(f"Joueur {current_player}, choisis une colonne (0-{COLS - 1}): "))

        # Insertion du jeton
        if insert_token(grid, col, current_player):
            # Vérifie si le joueur a gagné
            if check_win(grid, current_player):
                print_grid(grid)
                print(f"\nVictoire du joueur {current_player} 🎉")
                game_over = True
            else:
                # Changement de joueur
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Colonne pleine, choisis une autre !")

# ETAPE 8 
if __name__ == "__main__":
    # Initialisation de la grille
    grid = create_grid()

    # Jetons des deux joueurs
    players = ["X", "O"]
    current_player = 0  # 0 = X, 1 = O

    # Boucle principale de jeu
    while True:
        print_grid(grid)  # Affiche la grille actuelle

        # Demande au joueur courant de choisir une colonne
        col = int(input(f"Joueur {players[current_player]}, choisis une colonne (0-6) : "))

        # Tentative d'insertion du jeton
        if insert_token(grid, col, players[current_player]):
            # Vérification des victoires
            if (
                check_horizontal_win(grid, players[current_player])
                or check_vertical_win(grid, players[current_player])
                or check_diagonal_win(grid, players[current_player])
            ):
                print_grid(grid)
                print(f" Joueur {players[current_player]} a gagné !")
                break

            # Vérification égalité (grille pleine)
            if all(grid[0][c] != "." for c in range(COLS)):
                print_grid(grid)
                print("Match nul !")
                break

            # Changement de joueur (X -> O ou O -> X)
            current_player = 1 - current_player
        else:
            print(" Colonne pleine, choisis une autre !")




