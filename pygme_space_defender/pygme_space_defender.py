import pygame
import random

def main():

    #init pygame

    pygame.init()

    screen = pygame.display.set_mode((1500,600))

    pygame.display.set_caption('Defender')

    height = pygame.display.Info().current_h 
 
    width = pygame.display.Info().current_w

    FPS = 30 

    clock = pygame.time.Clock()

    # Random star generation
    slow_star_field = []
    med_star_field = []
    fast_star_field = []

    # How far stars should fall too
    stars_fall_too = 500
    
    # Make some stars

    for slow_star in range(50): 
        star_loc_x = random.randrange(0, width)
        star_loc_y = random.randrange(0, height)
        slow_star_field.append([star_loc_x, star_loc_y])


    for med_star in range(35): 
        star_loc_x = random.randrange(0, width)
        star_loc_y = random.randrange(0, height)
        med_star_field.append([star_loc_x, star_loc_y])

    for fast_star in range(15): 
        star_loc_x = random.randrange(0, width)
        star_loc_y = random.randrange(0, height)
        fast_star_field.append([star_loc_x, star_loc_y])

    # Make some colors

    WHITE = (255, 255, 255)
    LIGHTGREY = (192, 192, 192)
    DARKGREY = (128, 128, 128)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)

    # lets set up the score
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf',32)
    textX=10
    textY=525

    # Load the ship
    # TODO: this is broken
    playerImg = pygame.image.load('ship.png').convert()
    playerImg.set_colorkey(BLACK)


    def show_score(x,y):
        score = font.render("Score : " + str(score_value), True, (255,255,255))
        screen.blit(score,(x, y))



    #game loop

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill(BLACK)

        for star in slow_star_field:
            star[1] += 1
            if star[1] > stars_fall_too:
                star[0] = random.randrange(0, width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, DARKGREY, star, 3)

        for star in med_star_field:
            star[1] += 4
            if star[1] > stars_fall_too:
                star[0] = random.randrange(0, width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, LIGHTGREY, star, 2)

        for star in fast_star_field:
            star[1] += 8
            if star[1] > stars_fall_too:
                star[0] = random.randrange(0, width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, YELLOW, star, 1)

        
        pygame.draw.line(screen,GREEN,(0,500),(1500,500),4)

        # Show Score
        show_score(textX,textY)   

        # Display player
        screen.blit(playerImg,(round(10), round(200)))

        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()


