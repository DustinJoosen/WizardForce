import pygame
from widgets.Button import Button
import events.ButtonEvents
from Enums import EventType
from ScreenManager import ScreenManager

pygame.init()

WIDTH = 800
HEIGHT = 530

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wizard Force")

screen_manager = ScreenManager(screen)

running = True
while running:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT):
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			# print("mouse button down")
			pass

	#TODO: the functions of the buttons, are executed every frame. This is not desired.
	if len(events) > 0:
		screen_manager.event_handler.CheckEvents()

	screen_manager.Draw()
