from Enums import ScreenCode
from events.EventHandler import EventHandler
from data.DataContext import DataContext
import pygame


class ScreenManager:
	def __init__(self, screen):
		self.screen = screen

		self.screen_code = ScreenCode.IS_StartScreen
		self.event_handler = EventHandler()

		self.data_context = DataContext()
		self.data_context.InitProviders()

	def SetScreenCode(self, screen_code):
		self.screen_code = screen_code
		self.event_handler.Clear()

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

	def __DrawStartScreen(self):
		bg_sprite = pygame.image.load("../WizardForce/resources/sprites/backgrounds/mainscreen_bg.jpg")
		header_sprite = pygame.image.load("../WizardForce/resources/sprites/gametitle_header.png")

		self.screen.blit(bg_sprite, (0, 0))
		self.screen.blit(header_sprite, (117, 40))

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
