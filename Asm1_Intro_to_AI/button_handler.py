import pygame

class Button():
    def __init__(self, screen, height):
        self.screen = screen
        self.height = height

    def draw_buttons(self):
        #draw start button
        start_button = pygame.Rect(0, self.height - 95, 100, 50)
        pygame.draw.rect(self.screen, "green", start_button)
        self.screen.blit(pygame.font.Font(None, 24).render('Start', True, "white"), (20, self.height - 85))
        #draw stop button
        stop_button = pygame.Rect(300, self.height - 95, 100, 50)
        pygame.draw.rect(self.screen, "red", stop_button)
        self.screen.blit(pygame.font.Font(None, 24).render('Stop', True, "white"), (320, self.height - 85))
        #draw pause button
        pause_button = pygame.Rect(600, self.height - 95, 100, 50)
        pygame.draw.rect(self.screen, "blue", pause_button)
        self.screen.blit(pygame.font.Font(None, 24).render('Pause', True, "white"), (620, self.height - 85))
        #draw resume button
        resume_button = pygame.Rect(900, self.height - 95, 100, 50)
        pygame.draw.rect(self.screen, "yellow", resume_button)
        self.screen.blit(pygame.font.Font(None, 24).render('Resume', True, "black"), (920, self.height - 85))

