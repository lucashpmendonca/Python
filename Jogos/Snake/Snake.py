import pygame, random, time
from pygame.locals import *

def on_grid_random():        
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10 , y//10 * 10)

def on_grid_random2():        
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//20 * 20 , y//20 * 20)

def collision(c1, c2):
    return(c1[0] == c2[0] and c1[1] == c2[1]) 


def cores():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return ((r,g,b))

def tempo():
    
    while not game_over:
        time.sleep(1)
        contador.append(1)
        break
        
    return Int.contador

pygame.init()
screen = pygame.display.set_mode((600,600)) #tamanho tabuleiro
pygame.display.set_caption('Snake')

audio_maca = pygame.mixer.Sound('comeu.ogg') #audio comeu maça

contador = 0


# Definiçoes da cobra
snake =[(200, 200),(210, 200),(220,200)] 
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

# Definiçções da big maça
bigapple_pos = on_grid_random2()
bigapple = pygame.Surface((20,20))
bigapple.fill(cores())

# Definiçções da maça
apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

# direção do movimento
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

my_direction = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0


game_over = False

while not game_over:
    
    
    
    clock.tick(10) #definindo fps / velocidade da cobra
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    # Controles
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP

            if event.key == K_DOWN:
                my_direction = DOWN

            if event.key == K_RIGHT:
                my_direction = RIGHT

            if event.key == K_LEFT:
                my_direction = LEFT
                
    if collision(snake[0], apple_pos): # pegou a maça
        audio_maca.play() # play audio comeu maça
        apple_pos = on_grid_random() 
        snake.append((0,0))
        score = score + 1
        
    if collision(snake[0], bigapple_pos): # pegou a big maça
        bigapple.fill(cores())
        audio_maca.play()
        bigapple_pos = on_grid_random2()
        snake.append((0,0))
        score = score + 4
        
        
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0 : # borda
        game_over = True 
        break
    
    for i in range(1, len(snake)-1):  # bateu nela mesma
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break
        
    if game_over:
        break
        
    for i in range(len(snake) -1, 0, -1): 
        snake[i] = (snake[i - 1][0], snake[i - 1][1])
    
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
        
    
    
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    screen.blit(bigapple, bigapple_pos )
    
    for x in range(0,600,10): #desenha linhas verticais
        pygame.draw.line(screen,(40,40,40), (x,0 ),(x,600))
    for y in range(0,600,10): #desenha linhas verticais
        pygame.draw.line(screen,(40,40,40), (0 ,y ),(600, y)) 
        
        
        # Definições placar 
    score_font = font.render ('SCORE: %s' %(score), True , (255,255,255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 -120,10)
    screen.blit(score_font,score_rect)
    
    # Definições TEMPORIZADOR
    tempo_font = font
    tempo_screen = font.render ('TEMPO : '+ str(contador), True , (255,255,255))
    tempo_rect = tempo_screen.get_rect()
    tempo_rect.topleft = (600 -220,10)
    screen.blit(tempo_screen,tempo_rect)
    pygame.display.update()
    
    
    for pos in snake:
        screen.blit(snake_skin,pos)
        
    
    pygame.display.update()
    
while game_over:
    game_over_font = font #pygame.font.Font('freesansbold.ttf, 50')
    game_over_screen = game_over_font.render('GAME OVER', True , (255,255,255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop =(600 / 2 , 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            pygame.time.wait(500)
            pygame.quit()
            exit()
