import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("messi vs mbappé")

player_img = pygame.image.load('messi.png') 
player_size = 50
player_pos = [WIDTH / 2, HEIGHT - 2 * player_size]

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]


speed = 10
clock = pygame.time.Clock()
game_over = False
is_game_running = False


font = pygame.font.SysFont(None, 55)


def create_enemies():
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


def move_enemies():
    for enemy in enemy_list:
        if enemy[1] >= 0 and enemy[1] < HEIGHT:
            enemy[1] += speed
        else:
            enemy_list.remove(enemy)


def collision_detection(player_pos, enemy_list):
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False


def show_menu():
    screen.fill((255, 255, 255))
    start_text = font.render("Presiona ENTER para empezar", True, (0, 0, 0))
    quit_text = font.render("Presiona Q para salir", True, (0, 0, 0))
    screen.blit(start_text, (150, HEIGHT / 2 - 50))
    screen.blit(quit_text, (230, HEIGHT / 2 + 50))


def reset_game():
    global game_over, is_game_running, player_pos, enemy_list
    game_over = False
    is_game_running = False
    player_pos = [WIDTH / 2, HEIGHT - 2 * player_size]
    enemy_list = [enemy_pos]


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not is_game_running: 
                reset_game()
                is_game_running = True
            elif event.key == pygame.K_q: 
                pygame.quit()
                sys.exit()

            if is_game_running:
                x = player_pos[0]
                y = player_pos[1]

                if event.key == pygame.K_LEFT:
                    x -= player_size
                elif event.key == pygame.K_RIGHT:
                    x += player_size

                player_pos = [x, y]

    if not is_game_running:
        show_menu()
    else:
        screen.fill((0, 0, 0))

        
        create_enemies()
        move_enemies()

        if collision_detection(player_pos, enemy_list):
            reset_game()

        
        screen.blit(player_img, (player_pos[0], player_pos[1]))

        

        for enemy_pos in enemy_list:
            enemy_img = pygame.image.load('mbappe.png') 
            screen.blit(enemy_img, (enemy_pos[0], enemy_pos[1]))


        clock.tick(30)

    pygame.display.update()
