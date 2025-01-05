
import pygame
import sys
import random

# Inicializar o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 0)  # Amarelo
ROAD_COLOR = (128,128, 0)  # Cinza escuro
LANE_COLOR = (0, 0, 0)  # Branco
FPS = 500

# Inicializar a tela
tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("perspective")


# Inicializar posição do carro
pers_x = SCREEN_WIDTH // 2 
pers_y = SCREEN_HEIGHT //2



def draw_l():
    global pers_x
    global pers_y
    """Desenhar a estrada na tela."""
    pygame.draw.circle(tela, LANE_COLOR,(pers_x, pers_y), 20)
    pygame.draw.line(tela, LANE_COLOR, (0, 0), (pers_x, pers_y), 1)
    pygame.draw.line(tela, LANE_COLOR, (SCREEN_WIDTH, SCREEN_HEIGHT), (pers_x, pers_y), 1)
    pygame.draw.line(tela, LANE_COLOR, (0, SCREEN_HEIGHT), (pers_x, pers_y), 1)
    pygame.draw.line(tela, LANE_COLOR, (SCREEN_WIDTH, 0), (pers_x, pers_y), 1)
    pygame.draw.line(tela, LANE_COLOR, (SCREEN_WIDTH,SCREEN_HEIGHT//2), (pers_x, pers_y), 1)
    pygame.draw.line(tela, LANE_COLOR, (SCREEN_WIDTH//2, SCREEN_HEIGHT), (pers_x, pers_y), 1)
    pygame.draw.line(tela, LANE_COLOR, (0, SCREEN_HEIGHT//2), (pers_x, pers_y), 1)
    pygame.draw.line(tela, LANE_COLOR, (SCREEN_WIDTH//2, 0), (pers_x, pers_y), 1)
# Loop principal
def main():
    global pers_x
    global pers_y
    clock = pygame.time.Clock()
    running = True

    while running:
        tela.fill(BG_COLOR)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimento do carro
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pers_x -= 1
        if keys[pygame.K_RIGHT]:
            pers_x += 1
        if keys[pygame.K_UP]:
            pers_y -= 1
        if keys[pygame.K_DOWN]:
            pers_y += 1

        
        
        if pers_x>SCREEN_WIDTH:
            pers_x>SCREEN_WIDTH
        if pers_y>SCREEN_HEIGHT:
            pers_y>SCREEN_HEIGHT
        if pers_x<0:
            pers_x=0
        if pers_y<0:
            pers_y=0


        
        draw_l()
        

        # Atualizar tela
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
