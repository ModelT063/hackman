import pygame
import hackman
import random

def main():
    pygame.init()

    pygame.display.set_caption("testing")
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("monospace", 50)
    timer = pygame.time.Clock()
    display_time = 100
    delta = 0
    game = hackman.hackman()
    game.params["length"] = random.randint(4, 15)
    game.callAPI()
    
    running = True

    while running:
        for event in pygame.event.get():
            # KEYBOARD PRESS EVENT
            if event.type == pygame.KEYDOWN:
                # if user presses a letter, guess that letter
                if event.unicode.isalpha():
                    if not game.guessLetter(event.unicode):
                        display_time -= 10


            # CLOSE WINDOW EVENT
            elif event.type == pygame.QUIT:
                running = False
        
        if game.win() or display_time <= 0: 
            display_time = 100
            game.params["length"] = random.randint(4, 15)
            game.resetGame()
        
        # updates timer
        delta += timer.tick()
        if(delta > 1000):  
            delta = 0
            display_time -= 1

        screen.fill((0,0,0))
        text = font.render(game.displayWord, False, (255,255,255), (0,0,0))               
        screen.blit(text, (100, 100))
        text = font.render(str(display_time), False, (255, 255, 255), (0,0,0))
        screen.blit(text, (100, 200))
        pygame.display.update()

if __name__ == "__main__":
    main()