import pygame
import random

pygame.init()
pygame.mixer.init()

# * Color
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
forest_green = 	(34,100,34)
green = (0,128,0)
blue = (0,0,255)

# * Creating window
screen_width = 800
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width,screen_height))


# * Creating Title
pygame.display.set_caption("Snake Game")
pygame.display.update()


play_music = True
fps = 30
clock = pygame.time.Clock()


def text_screen(text, color,font_size, x, y):
    '''
    this is a function for writting text on the screen
    'test' -(str)->  string that will be display
    'color' -(touple)->  the color in which the text will be print
    'font_size' -(int)-> the size of the font 
    'x,y' -(int)->  the cordinate where text will be printed
    '''
    font = pygame.font.SysFont(None, font_size)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snake_body, snake_size):
    '''
    this function plot the snake in the screen  
    '''
    for x,y in snake_body[:-1]:
        pygame.draw.rect(gameWindow, color[1], [x, y, snake_size, snake_size])
    x,y = snake_body[-1]
    pygame.draw.rect(gameWindow, color[0], [x, y, snake_size, snake_size])

def welcome_screen():
    '''
    this function create the welcome screen
    '''
    # Background Image for Welcome Screen
    bgimg = pygame.image.load("resources/welcome_page.jpeg")
    bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
    gameWindow.blit(bgimg, (0,0))

    # Background Music
    pygame.mixer.music.load('resources/bmg.ogg')
    pygame.mixer.music.play(-1)

    # print test on the screen
    text_screen("Welcome To Snack Game",red,50,190,200)
    text_screen("Press Any Key to Start",black,50,220,250)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                game_loop()
        clock.tick(fps)


def game_paused():
    '''
    this function helps to pause the game
    '''
    text_screen("Game Paused",black,65,270,200)
    text_screen("Press Spacebar to Continue",black,50,200,250)
    pygame.display.update()
    
    pygame.mixer.music.pause()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.unpause()
                    return
        clock.tick(fps)


def game_over():
    '''
    this is a function for the game over method
    '''
    
    text_screen("Game Over",black,65,290,200)
    text_screen("Press Enter to Continue",black,50,220,250)

    pygame.mixer.music.pause()
    sound= pygame.mixer.Sound("resources/game_over.ogg")
    pygame.mixer.Sound.play(sound)

    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.unpause()
                    game_loop()
        clock.tick(fps)

# Creating a game loop
def game_loop():
    '''
    this is the main function the runs the game
    '''
    # Game specific variables
    exit_game = False
    global play_music

    snake_x = screen_width/2
    snake_y = screen_height/2
    snake_size = 30
    snake_body = []
    snake_length = 1

    velocity = 3
    velocity_x = velocity
    velocity_y = 0

    move_x = False
    move_y = True

    food_x = 400
    food_y = 300
    food_size = 12

    score = 0

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and move_x == True:
                    velocity_x = velocity
                    velocity_y = 0
                    move_x = False
                    move_y = True
                if event.key == pygame.K_LEFT and move_x == True:
                    velocity_x = -velocity
                    velocity_y = 0
                    move_x = False
                    move_y = True
                if event.key == pygame.K_UP and move_y == True:
                    velocity_x = 0
                    velocity_y = -velocity
                    move_x = True
                    move_y = False
                if event.key == pygame.K_DOWN and move_y == True:
                    velocity_x = 0
                    velocity_y = velocity
                    move_x = True
                    move_y = False
                if event.key == pygame.K_SPACE:
                    game_paused()
                if event.key == pygame.K_m:
                    if play_music:
                        pygame.mixer.music.pause()
                        play_music = False
                    else:
                        pygame.mixer.music.play()
                        play_music = True

        # snake possition updating             
        snake_x = snake_x + velocity_x
        snake_y = snake_y + velocity_y
        
        snake_head = [snake_x,snake_y]
        snake_body.append(snake_head)
        
        # game condition/rules
        if len(snake_body)>snake_length:
            del snake_body[0]
        
        if snake_head in snake_body[:-1]:
            game_over()
        
        if snake_x<5 or snake_x>(screen_width - 35) or snake_y<75 or snake_y>(screen_height - 35):
            game_over()
        
        if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
            sound= pygame.mixer.Sound("resources/kill.wav")
            pygame.mixer.Sound.play(sound)
            
            score = score + 1
            food_x = random.randint(30, screen_width - 30)
            food_y = random.randint(100, screen_height - 30)
            snake_length = snake_length + 5
        
        # game Window
        gameWindow.fill(white)
        pygame.draw.rect(gameWindow,red,[0,70,screen_width,screen_height - 70],10)
        text_screen(f"Player Score: {score * 10}", black, 55, 5, 5)
        pygame.draw.circle(gameWindow,blue,[food_x, food_y],food_size)
        plot_snake(gameWindow, (forest_green,green), snake_body, snake_size)
        
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


welcome_screen()