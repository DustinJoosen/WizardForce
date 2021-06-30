import pygame
from widgets.Button import Button
import events.ButtonEvents
from Enums import EventType
from events.EventHandler import EventHandler
from data.DataContext import DataContext

pygame.init()

WIDTH = 800
HEIGHT = 530

button = Button([0, 0], [80, 80], events.ButtonEvents.OpenScreen, EventType.Both, 'IS_Mainscreen')

event_handler = EventHandler()
event_handler.AddWidget(button)

data_context = DataContext()
data_context.InitProviders()

wizards = data_context.Wizard.GetAll()

screen = pygame.display.set_mode((WIDTH, HEIGHT))


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#TODO: the functions of the buttons, are executed every frame. This is not desired
	event_handler.CheckEvents()

	pygame.draw.rect(screen, (255, 255, 255), (0, 0, 80, 80))
	pygame.display.update()
