import pygame
import hackman

def main():
    pygame.init()

    pygame.display.set_caption("testing")
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("monospace", 50)
    game = hackman.hackman()
    game.callAPI()
    
    running = True

    while running:
        for event in pygame.event.get():
            # KEYBOARD PRESS EVENT
            if event.type == pygame.KEYDOWN:
                # if user presses a letter, guess that letter ######### FIX THIS ALL EVENT KEYS RETURN ALPHA ################
                if pygame.key.name(event.key)[-1].isalpha():
                    game.guessLetter(pygame.key.name(event.key)[-1])

            # CLOSE WINDOW EVENT
            elif event.type == pygame.QUIT:
                running = False
                
        if game.win(): 
            game.resetGame()
        text = font.render(game.displayWord, False, (255,255,255))               
        screen.blit(text, (100, 100))
        pygame.display.update()

if __name__ == "__main__":
    main()