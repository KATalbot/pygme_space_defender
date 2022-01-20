import pygame

def main():

    screen = pygame.display.set_mode((1024,768))

    height = pygame.display.Info().current_h
    width = pygame.display.Info().current_w

    star_field_slow = []

    for slow_stars in range(50): 
        star_loc_x = random.randrange(0, width)
        star_loc_y = random.randrange(0, height)
        star_field_slow.append([star_loc_x, star_loc_y])


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

    pygame.init()

    

    #game loop

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                running = False

        screen.fill(BLACK)
       
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()


