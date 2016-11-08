import pygame
import time
import random
import pickle
pygame.init()
display_width=400
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
block_color=(53,112,85)
carData=[]


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit racy')
clock = pygame.time.Clock()
carImg=  pygame.image.load('car.png')
car_width = 54

def things_dodged(count):
    font=pygame.font.SysFont(None,25)
    text= font.render("Dodged: "+str(count),True,black)
    gameDisplay.blit(text,(0,0))

    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',40)
    TextSurf,TextRect= text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

    time.sleep(2)
    gameLoop()


def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
    

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def crash():
    message_display('You Crashed')


def grabData(x,thingx,thingy,thingSpeed,xChange):
    temp=[]
    temp.append(thingx)
    temp.append(thingy)
    
    temp.append(thingSpeed)
    temp.append(xChange)
    carData.append(temp)
    
    
    
    



def gameLoop():

    
    x = (display_width*0.45)
    y = (display_height*0.8)

    x_change=0

    thing_startx =  random.randrange(0,display_width)
    thing_starty = 0
    thing_speed=15
    thing_width=100
    thing_height=100
    block_color=black

    dodged=0

    carData_pickle = open("carDat.pickle","wb")
    
    

    gameExit = False

    while not gameExit:
        inputdata=[]
        inputdata.append(int(x))
        inputdata.append(thing_startx)
        inputdata.append(thing_starty)
        inputdata.append(thing_speed)
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pickle.dump(carData,carData_pickle)
                print(carData)
                carData_pickle.close()
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-10
                elif event.key==pygame.K_RIGHT:
                    x_change=10

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                  x_change=0
            
        
##        x_change=clf.predict(inputdata)
##        print(inputdata,int(x_change))
        x+=int(x_change)
                

           # print(event)
        gameDisplay.fill(white)


        things(thing_startx,thing_starty,thing_width,thing_height,block_color)
        thing_starty+=thing_speed
        car(x,y)
        grabData(x,thing_startx,thing_starty,thing_speed,x_change)
        things_dodged(dodged)

        if x >display_width-car_width or x<0:
            crash()

        if thing_starty>display_height:
            thing_starty=0
            thing_startx=random.randrange(0,display_width)
            dodged+=1
            #thing_speed+=1
            block_color=(random.randrange(0,200),random.randrange(0,200),random.randrange(0,200))
            thing_width=random.randrange(30,80)

        if y<thing_starty+thing_height:
            if x>thing_startx and x<thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
                crash()

        
        pygame.display.update()
        clock.tick(10)

gameLoop()
pygame.quit()
quit()
