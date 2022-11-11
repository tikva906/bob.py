import pygame

class Bob_glavnii:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

 #создаем функцыю
    def Start(self):
        while True:
            self.screen.fill((244,244,0))
            # Обновление экрана (fps)
            pygame.display.flip()

if __name__ == '__main__':
    game = Bob_glavnii()
    game.Start()