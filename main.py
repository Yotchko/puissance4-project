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
