print('Programa que abra e reproduza o audio de um arquivo MP3')

import pygame
pygame.init()
pygame.mixer.music.load('Piratas_do_Caribe_Intro.mp3')
pygame.mixer.music.play()
pygame.event.wait()
