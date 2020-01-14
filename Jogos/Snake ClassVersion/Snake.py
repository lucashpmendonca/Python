import pygame, sys
from pygame.locals import *
from random import randint


BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0, 255, 0)
GRAY = (200,200,200)

#Directions
UP = 8
DOWN = 2
LEFT = 4
RIGHT = 6

global clock
clock = pygame.time.Clock()

#Classes

class Game():

    #Initialize 

    def __init__(self,width,height,clock):

        pygame.init()
        #Caption window
        pygame.display.set_caption('Snake')
        self.width=width
        self.height=height
        self.screen=pygame.display.set_mode((self.width,self.height))
        #Background
        self.background=pygame.Surface(self.screen.get_size())
        self.background.fill(BLACK)
        self.background.convert()
        #Score Card
        self.scorecard=pygame.draw.rect(self.background,GREEN,Rect([10,10],[self.width - 20,50]),1)
        #Game area draw
        self.gamearea=pygame.draw.rect(self.background,GREEN,Rect([10,70],[self.width - 20,self.height - 70]),1)
        self.points=0
        
        #Score
        self.font=pygame.font.Font(None,36)
        clock = pygame.time.Clock()
        self.fps= clock
        self.snake=Snake()
        self.food=Food(self.snake)
        self.bigfood=BigFood(self.snake)

    def run(self):
        """Main Loop
        """
        dead=0

        while not dead:
            
            #Speed
            if self.points>100:
                clock.tick(30) 
            elif self.points>200:
                clock.tick(50) 
            else:
                if self.points>300:
                    clock.tick(60) 
                elif self.points>400:
                    clock.tick(70) 
                else:
                    clock.tick(15) 

            #Quit event
            for event in pygame.event.get():
                if event.type == QUIT: 
                    pygame.quit()
                    sys.exit()
                #<ESC> to quit
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                

                if event.type == KEYDOWN:
                #Changing direction
                    if ((event.key == K_LEFT or event.key == ord('o'))
                        and self.snake.direction!=RIGHT):
                            self.snake.direction=LEFT
                    elif ((event.key == K_RIGHT or event.key == ord('p'))
                        and self.snake.direction!=LEFT):
                            self.snake.direction=RIGHT
                    elif ((event.key == K_UP or event.key == ord('q'))
                        and self.snake.direction!=DOWN):
                            self.snake.direction=UP
                    elif ((event.key == K_DOWN or event.key == ord('a'))
                        and self.snake.direction!=UP):
                            self.snake.direction=DOWN
                            
            
            

            #Updates the head
            dead=self.snake.update(self.snake.direction,self.width,self.height)

            #Checks if head is eating body
            if self.snake.body.count(self.snake.head)>0:
                dead=1

            #Inserts the new head into the body
            self.snake.body.insert(0,list(self.snake.head))

            #Eat food
            if self.snake.head[0]==self.food.foodXY[0] and self.snake.head[1]==self.food.foodXY[1]:
                self.food=Food(self.snake)
                self.incPoints()
                
            else:
                #removes the tail
                self.snake.body.pop()
                '''
            for x in range(0,600,10): #desenha linhas verticais
                pygame.draw.line(self.screen,(40,40,40), (x,0 ),(x,600))
            for y in range(0,600,10): #desenha linhas verticais
                pygame.draw.line(self.screen,(40,40,40), (0 ,y ),(600, y))'''
            #self.clock.tick(self.fps)
            self.drawScore()
            self.drawTime()
            self.drawSnake()
            self.drawFood()
            
            pygame.display.update()
            self.screen.blit(self.background,(0,0))
            

        pygame.quit()

    def incPoints(self):
        self.points=self.points+100

    def drawScore(self):
        surface = self.font.render("Points: "+str(self.points), True, GRAY)
        self.screen.blit(surface, (15, 25))

    def drawTime(self):
        total_segs = pygame.time.get_ticks()/1000
        horas = total_segs // 3600
        segs_restantes = total_segs % 3600
        minutos = segs_restantes // 60
        segs_restantes_final = segs_restantes % 60
        contador = (str(int(horas))+':'+str(int(minutos))+':'+str(round(segs_restantes_final,1)))

        time = self.font.render ('TEMPO : '+str(contador), False , (255,255,255))
        self.screen.blit(time, (200, 25))

    def drawSnake(self):
        for x in self.snake.body:
            pygame.draw.rect(self.screen,GREEN, Rect(x,(10,10)))

    def drawFood(self):
        pygame.draw.rect(self.screen,RED, Rect(self.food.foodXY,(10,10)))
        
    def drawBigFood(self):
        pygame.draw.rect(self.screen,RED, Rect(self.bigfood.bigfoodXY,(40,40)))
    

class Snake():
    
    def __init__(self):
        x1=randint(0,10)
        y1=randint(0,10)
        x=int(x1*20)+10
        y=int(y1*20)+120
        self.head = [x,y]

        self.body = [[x,y],[x,y]]
        self.direction = RIGHT

    def update(self,direction,width,height):
        """Updates the head position of the snake.
        Returns 1 if head is off-limits on the game area.
        """
        if direction==RIGHT:
            self.head[0]+=10
            self.direction=RIGHT
            if self.head[0] > width-10:
                return 1
            else:
                return 0
        elif direction==LEFT:
            self.head[0]-=10
            self.direction=LEFT
            if self.head[0] < 10:
                return 1
            else:
                return 0
        elif direction==UP:
            self.head[1]-=10
            self.direction=UP
            if self.head[1] < 70:
                return 1
            else:
                return 0
        elif direction==DOWN:
            self.head[1]+=10
            self.direction=DOWN
            if self.head[1] > height-20:
                return 1
            else:
                return 0


class Food():
    def __init__(self,snake):
        while True:
            x1=randint(0,20)
            y1=randint(0,17)
            self.foodXY=[int(x1*20)+10,int(y1*20)+120]
            if snake.body.count(self.foodXY)==0:
                break

class BigFood():
    def __init__(self,snake):
        while True:
            x1=randint(0,20)
            y1=randint(0,17)
            self.bigfoodXY=[int(x1*20)+10,int(y1*20)+120]
            if snake.body.count(self.bigfoodXY)==0:
                break


#Main

if __name__ == "__main__":
    #call
    Game(600,600,10).run()