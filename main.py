
# ETAPE 1
# Définition des dimensions de la grille
ROWS = 6  # Nombre de lignes
COLS = 7  # Nombre de colonnes

# Fonction pour créer une grille vide 6x7
def create_grid():
    # On utilise une liste de listes pour représenter les cases
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

# Fonction pour afficher la grille dans la console
def print_grid(grid):
    for row in grid:
        # On affiche chaque ligne avec des | entre les cases
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
# Le jeton tombe dans la première case vide en partant du bas
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








