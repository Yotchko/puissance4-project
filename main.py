
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








