""""
Un jeu où le but est d'ordonner la grille. Pour effectuer un swap on clique avec la souris sur une case et on tire le chiffre 
vers une case adjacente.

"""

import pygame
import random
import time

# On initialise Pygame
pygame.init()

WINDOW_SIZE = (500, 500)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Grid Swap Game")

# On definit les codes rgb des couleurs
PINK1 = (255, 105, 180)
WHITE = (255, 255, 255)
PINK2 = (248, 200, 220)
YELLOW = (255, 255, 0)

# On détermine les dimensions de la grille
GRID_SIZE = (3, 3)  

# On définit le taille des carreaux pour être adéquate à la grille pour bien remplir notre fenêtre
TILE_SIZE = min(WINDOW_SIZE[0] // GRID_SIZE[1], WINDOW_SIZE[1] // GRID_SIZE[0])

# On initialise la grille avec des nombres aléatoires entre 1 et n*m
numbers = list(range(1, GRID_SIZE[0] * GRID_SIZE[1] + 1))
random.shuffle(numbers)
grid = [numbers[i * GRID_SIZE[1]:(i + 1) * GRID_SIZE[1]] for i in range(GRID_SIZE[0])]

# On fait tourner le jeu
running = True
selected_tile = None
swap_count = 0
won = False

def celebrate():
    for _ in range(2):
        for i in range(GRID_SIZE[0]):
            for j in range(GRID_SIZE[1]):
                rect = pygame.Rect(j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, YELLOW, rect)
                pygame.display.flip()
                time.sleep(0.1)
                pygame.draw.rect(screen, WHITE, rect)
                pygame.display.flip()
                time.sleep(0.1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # On prend note du carreau qu'on a cliqué
            pos = pygame.mouse.get_pos()
            row, col = pos[1] // TILE_SIZE, pos[0] // TILE_SIZE
            if 0 <= row < GRID_SIZE[0] and 0 <= col < GRID_SIZE[1]:
                selected_tile = (row, col)

        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_tile:
                # On performe le swap
                row, col = event.pos[1] // TILE_SIZE, event.pos[0] // TILE_SIZE
                if (0 <= row < GRID_SIZE[0] and 0 <= col < GRID_SIZE[1] and
                    (abs(row - selected_tile[0]) + abs(col - selected_tile[1]) == 1)):
                    grid[row][col], grid[selected_tile[0]][selected_tile[1]] = (
                        grid[selected_tile[0]][selected_tile[1]], grid[row][col])
                    swap_count += 1 # on compte à chaque fois qu'on fait un swap
                selected_tile = None

    # Verification de si la grille est rangée en ordre croissant
    sorted_grid = [item for row in grid for item in row]
    if sorted_grid == list(range(1, GRID_SIZE[0] * GRID_SIZE[1] + 1)):
        print(f"Congratulations! You beat the game in {swap_count} swaps!")
        won = True
        celebrate()
        running = False

    # On dessine la grille
    screen.fill(WHITE)
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            rect = pygame.Rect(j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, PINK2, rect, 3)
            value = grid[i][j]
            text = pygame.font.Font(None, int(TILE_SIZE * 0.6)).render(str(value), True, PINK1)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()