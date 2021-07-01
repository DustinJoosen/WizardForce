from Enums import ScreenCode, EventType
from events.EventHandler import EventHandler
from widgets.Button import Button
import events.ButtonEvents
from data.DataContext import DataContext
import pygame


class ScreenManager:
	def __init__(self, screen):
		self.screen = screen

		#all the events can be managed via the event handelr
		self.event_handler = EventHandler()

		#a dictionary to store the loaded images in
		self.images = {}

		#init the data context + providers
		self.data_context = DataContext()
		self.data_context.InitProviders()

		#init the screen
		self.screen_code = None
		self.SetScreenCode(ScreenCode.IS_StartScreen)

	def SetScreenCode(self, screen_code):
		self.screen_code = screen_code
		self.event_handler.Clear()

		if self.screen_code == ScreenCode.IS_StartScreen:
			self.__InitStartScreen()
		#this can be extended, like the Draw() method

	#calls the correct method, related to the current screen_code
	def Draw(self):
		if self.screen_code == ScreenCode.IS_StartScreen:
			self.__DrawStartScreen()
		elif self.screen_code == ScreenCode.IS_MainScreen:
			self.__DrawMainScreen()
		elif self.screen_code == ScreenCode.IS_SettingsScreen:
			self.__DrawSettingsScreen()
		elif self.screen_code == ScreenCode.IS_PartyScreen:
			self.__DrawPartyScreen()
		elif self.screen_code == ScreenCode.IS_ShopScreen:
			self.__DrawShopScreen()
		elif self.screen_code == ScreenCode.IS_BattleScreen:
			self.__DrawBattleScreen()

		pygame.display.update()

	#InitMethods initialize the events, images and buttons of the current screen
	def __InitStartScreen(self):
		self.images["bg_sprite"] = pygame.image.load("../WizardForce/resources/sprites/backgrounds/mainscreen_bg.jpg")
		self.images["header_sprite"] = pygame.image.load("../WizardForce/resources/sprites/gametitle_header.png")

		button = Button([0, 0], [40, 40], EventType.OnClick, events.ButtonEvents.CloseScreen)
		self.event_handler.AddWidget(button)

	#DrawMethods draw the images and objects onto the screen
	def __DrawStartScreen(self):
		self.screen.blit(self.images["bg_sprite"], (0, 0))
		self.screen.blit(self.images["header_sprite"], (117, 40))

		for widget in self.event_handler.GetWidgets():
			widget.Draw(self.screen)

	def __DrawMainScreen(self):
		pass

	def __DrawSettingsScreen(self):
		pass

	def __DrawPartyScreen(self):
		pass

	def __DrawShopScreen(self):
		pass

	def __DrawBattleScreen(self):
		pass
