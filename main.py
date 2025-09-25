
# PUISSANCE 4 JEU


# ETAPE 1 : Définition des dimensions de la grille
ROWS = 6  # Nombre de lignes
COLS = 7  # Nombre de colonnes

# ETAPE 1 partie 2 : Création d'une grille vide
def create_grid():
    """Crée une grille vide 6x7"""
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

# ETAPE 1 partie 3 : Affichage de la grille
def print_grid(grid):
    """Affiche la grille dans la console"""
    for row in grid:
        print("|".join(row))
    print("-" * (2 * COLS - 1))

# ETAPE 2 : Insertion d'un jeton
def insert_token(grid, col, token):
    """
    Insère un jeton dans la colonne spécifiée.
    Retourne True si l’insertion réussit, False si la colonne est pleine.
    """
    for row in reversed(range(ROWS)):
        if grid[row][col] == " ":
            grid[row][col] = token
            return True
    return False

# ETAPE 3 : Vérification victoire horizontale
def check_horizontal_win(grid, token):
    """Vérifie si le joueur a 4 jetons consécutifs horizontalement"""
    for row in grid:
        count = 0
        for cell in row:
            if cell == token:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

# ETAPE 4 : Vérification victoire verticale
def check_vertical_win(grid, token):
    """Vérifie si le joueur a 4 jetons consécutifs verticalement"""
    for col in range(COLS):
        count = 0
        for row in range(ROWS):
            if grid[row][col] == token:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

# ETAPE 5 : Vérification victoire diagonale
def check_diagonal_win(grid, token):
    """Vérifie si le joueur a 4 jetons consécutifs en diagonale"""
    # diagonales (haut vers bas)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (grid[row][col] == token and
                grid[row + 1][col + 1] == token and
                grid[row + 2][col + 2] == token and
                grid[row + 3][col + 3] == token):
                return True
    # diagonales (bas vers haut)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if (grid[row][col] == token and
                grid[row - 1][col + 1] == token and
                grid[row - 2][col + 2] == token and
                grid[row - 3][col + 3] == token):
                return True
    return False

# ETAPE 6 : Vérification victoire globale
def check_win(grid, token):
    """Vérifie victoire horizontale, verticale ou diagonale"""
    return (check_horizontal_win(grid, token) or
            check_vertical_win(grid, token) or
            check_diagonal_win(grid, token))



# ETAPE 7 : Boucle principale du jeu
def play_game():
    grid = create_grid()
    players = ["X", "O"]
    current_player = 0  # 0 = X, 1 = O
    game_over = False

    while not game_over:
        print_grid(grid)
        col = int(input(f"Joueur {players[current_player]}, choisis une colonne (0-{COLS - 1}) : "))

        if insert_token(grid, col, players[current_player]):
            if check_win(grid, players[current_player]):
                print_grid(grid)
                print(f"🎉 Joueur {players[current_player]} a gagné !")
                game_over = True
            elif is_full(grid):
                print_grid(grid)
                print("Match nul ! La grille est pleine.")
                game_over = True
            else:
                # Changement de joueur
                current_player = 1 - current_player
        else:
            print("Colonne pleine, choisis une autre !")

# ETAPE 8 : Détection match nul
def is_full(grid):
    """Retourne True si la grille est pleine, False sinon"""
    for row in grid:
        if " " in row:
            return False
    return True


# POINT D'ENTRÉE DU PROGRAMME

if __name__ == "__main__":
    print("===== Bienvenue dans le jeu Puissance 4 =====")
    print("Deux joueurs s'affrontent : X et O")
    print("Choisissez une colonne entre 0 et 6 pour placer votre jeton.\n")
    
    play_game()  # Lance directement le jeu
