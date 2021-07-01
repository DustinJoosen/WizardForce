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

clock = pygame.time.Clock()
FPS = 24

screen_manager = ScreenManager(screen)

while screen_manager.running:
	clock.tick(FPS)

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT):
			screen_manager.running = False

	#only check the events, if something actually happened.
	if len(events) > 0:
		screen_manager.event_handler.CheckEvents()

	screen_manager.Draw()
