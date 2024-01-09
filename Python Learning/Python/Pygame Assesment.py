import pygame
import time
pygame.init()
FPS= 30

#define colours
#colour = (RRR,GGG,BBB)
red= (255,0,0)
blue= (0,0,255)
black=(0,0,0)
white= (255,255,255)

#screen size
display_width = 800
display_height = 600

#The Screen Game Window Parameters
gameDisplay= pygame.display.set_mode ((display_width,display_height))

#Title of game
pygame.display.set_caption ('Slither.io')


#to manage FPS
clock= pygame.time.Clock()

#size of blocks
block_size=10

#font style
font= pygame.font.SysFont(None, 25)
def message_to_screen(msg,colour):
  screen_text= font.render(msg, True, colour)
  gameDisplay.blit(screen_text, [display_width/2, display_height/2])

def gameLoop():
  gameExit = False
  gameOver= False
  #position of snake head
  lead_x = display_width/2
  lead_y= display_height/2
  lead_x_change = 0
  lead_y_change = 0
  while not gameExit:
    while gameOver == True:
      gameDisplay.fill(white)
      message_to_screen("Game over, Press C to play again or Q to quit", blue)
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            gameExit= True
            gameOver =False
          if event.key == pygame.K_c:
            gameLoop()
  
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        gameExit = True
    #Whenever a certain key is pressed    
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          lead_x_change = -block_size
          lead_y_change = 0
        elif event.key ==  pygame.K_RIGHT:
          lead_x_change = block_size
          lead_y_change = 0
          
        elif event.key == pygame.K_UP:
          lead_x_change = 0
          lead_y_change = -block_size
        elif event.key ==  pygame.K_DOWN:
          lead_x_change = 0
          lead_y_change = block_size

    if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
      gameOver= True
    #change how fast the blocks move in a direction
    lead_x += lead_x_change
    lead_y += lead_y_change
    #colour of background
    gameDisplay.fill (white)
    #to draw a shape within the game window
    pygame.draw.rect (gameDisplay, black, [lead_x,lead_y,block_size,block_size])
    pygame.display.update()
    #fps rate
    clock.tick(FPS)
  #To quit program completetly
  pygame.quit()
  quit()

gameLoop()
