import pygame
import time
import random

pygame.init()

yellow=(255,255,102)
green=(0,255,0)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
nblue=(50, 153, 213)

dis_width=600
dis_height=400

disp=pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Game by Harshit Gupta")

clock=pygame.time.Clock()

snake=10
snake_speed=12

font_sytal=pygame.font.SysFont("bahnschrift", 25)
Score_font=pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    scor=font_sytal.render("Your Score: "+str(score), True,yellow)
    disp.blit(scor,[0,0])

def our_snake(snake, snake_List):
    for x in snake_List:
        pygame.draw.rect(disp,green,[x[0],x[1],snake,snake])

def message(msg,color):
    mesg=font_sytal.render(msg,True,color)
    disp.blit(mesg, [dis_width/6, dis_height/3])

def gameloop():
    game_over=False
    game_close=False

    x1=dis_width/2
    y1=dis_height/2

    x1_change=0
    y1_change=0

    snake_List=[]
    Length_of_Snake=1

    foodx=round(random.randrange(0,dis_width-snake)/10.0)*10.0
    foody=round(random.randrange(0,dis_height-snake)/10.0)*10.0

    while not game_over:

        while game_close==True:
            disp.fill(white)
            message("You Lost! Press Q-Quit or C-Play",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                elif event.key==pygame.K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                elif event.key==pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake
                elif event.key==pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake

        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close=True

        x1+=x1_change
        y1+=y1_change

        disp.fill(nblue)
        pygame.draw.rect(disp,blue,[foodx,foody,snake,snake])

        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        pygame.display.update()
        if len(snake_List)>Length_of_Snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x==snake_Head:
                game_close = True

        pygame.display.update()

        our_snake(snake,snake_List)
        your_score(Length_of_Snake-1)

        pygame.display.update()

        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0,dis_width-snake)/10.0)*10.0
            foody=round(random.randrange(0,dis_height-snake)/10.0)*10.0
            Length_of_Snake+=1

        clock.tick(snake_speed)
    pygame.quit()
    quit()

gameloop()
