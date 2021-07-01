from Enums import ScreenCode, EventType
from events.EventHandler import EventHandler
from widgets.Button import Button
from events.ButtonEvents import ButtonEvents
from data.DataContext import DataContext
import pygame


class ScreenManager:
	def __init__(self, screen):
		self.screen = screen
		self.running = True

		#allow the events to interact with the screen
		ButtonEvents.screen_manager = self

		#all the events can be managed via the event handeler
		self.event_handler = EventHandler()

		#a dictionary to store the loaded images in
		self.images = {}
		self.text_surfaces = {}

		#init the data context + providers
		self.data_context = DataContext()
		self.data_context.InitProviders()

		self.__font = pygame.font.SysFont('Cambria', 30)

		#init the screen
		self.screen_code = ScreenCode.IS_StartScreen
		self.SetScreenCode(self.screen_code)

	def SetScreenCode(self, screen_code):
		self.screen_code = screen_code
		self.event_handler.Clear()

		if self.screen_code == ScreenCode.IS_StartScreen:
			self.__InitStartScreen()
		elif self.screen_code == ScreenCode.IS_MainScreen:
			self.__InitMainScreen()
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
		root = "../WizardForce/resources/sprites"
		self.images["bg_sprite"] = pygame.image.load(f"{root}/backgrounds/mainscreen_bg.jpg")
		self.images["header_sprite"] = pygame.image.load(f"{root}/gametitle_header.png")
		self.images["mainmenu_option"] = pygame.image.load(f"{root}/buttons/mainmenu_option.png")

		self.text_surfaces["sp"] = self.__font.render("Singleplayer", False, (255, 255, 255))
		self.text_surfaces["op"] = self.__font.render("Settings", False, (255, 255, 255))
		self.text_surfaces["ex"] = self.__font.render("Exit", False, (255, 255, 255))

		sp_button = Button([245, 195], [310, 90], EventType.OnClick, ButtonEvents.OpenScreen,
						args=ScreenCode.IS_MainScreen, image=self.images["mainmenu_option"])
		op_button = Button([245, 290], [310, 90], EventType.OnClick, ButtonEvents.OpenScreen,
						args=ScreenCode.IS_SettingsScreen, image=self.images["mainmenu_option"])
		ex_button = Button([245, 385], [310, 90], EventType.OnClick, ButtonEvents.CloseGame,
						image=self.images["mainmenu_option"])

		self.event_handler.AddWidgets([sp_button, op_button, ex_button])

	def __InitMainScreen(self):
		root = "../WizardForce/resources/sprites"
		self.images["generic_bg_sprite"] = pygame.image.load(f"{root}/backgrounds/generic_bg.jpg")
		self.images["mainscreen_btn_sprite"] = pygame.image.load(f"{root}/buttons/mainscreen_button.png")
		self.images["map_sprite"] = pygame.image.load(f"{root}/map.png")

		self.text_surfaces["party"] = self.__font.render("Party", False, (255, 255, 255))
		self.text_surfaces["shop"] = self.__font.render("Shop", False, (255, 255, 255))
		self.text_surfaces["exit"] = self.__font.render("Exit", False, (255, 255, 255))

		if self.text_surfaces["op"] is None:
			self.text_surfaces["op"] = self.__font.render("Settings", False, (255, 255, 255))

		party_button = Button([640, 100], [140, 60], EventType.OnClick, ButtonEvents.OpenScreen,
							args=ScreenCode.IS_PartyScreen, image=self.images["mainscreen_btn_sprite"])
		shop_button = Button([640, 170], [140, 60], EventType.OnClick, ButtonEvents.OpenScreen,
							args=ScreenCode.IS_ShopScreen, image=self.images["mainscreen_btn_sprite"])
		settings_button = Button([640, 240], [140, 60], EventType.OnClick, ButtonEvents.OpenScreen,
							args=ScreenCode.IS_SettingsScreen, image=self.images["mainscreen_btn_sprite"])
		exit_button = Button([640, 310], [140, 60], EventType.OnClick, ButtonEvents.CloseGame,
							image=self.images["mainscreen_btn_sprite"])

		self.event_handler.AddWidgets([party_button, shop_button, settings_button, exit_button])

	#DrawMethods draw the images and objects onto the screen
	def __DrawStartScreen(self):
		self.screen.blit(self.images["bg_sprite"], (0, 0))
		self.screen.blit(self.images["header_sprite"], (117, 40))

		for widget in self.event_handler.GetWidgets():
			widget.Draw(self.screen)

		self.screen.blit(self.text_surfaces["sp"], (310, 220))
		self.screen.blit(self.text_surfaces["op"], (350, 315))
		self.screen.blit(self.text_surfaces["ex"], (385, 410))

	def __DrawMainScreen(self):
		self.screen.blit(self.images["generic_bg_sprite"], (0, 0))
		self.screen.blit(self.images["map_sprite"], (35, 60))

		for widget in self.event_handler.GetWidgets():
			widget.Draw(self.screen)

		self.screen.blit(self.text_surfaces["op"], (650, 110))
		self.screen.blit(self.text_surfaces["party"], (670, 180))
		self.screen.blit(self.text_surfaces["shop"], (675, 250))
		self.screen.blit(self.text_surfaces["ex"], (680, 320))

	def __DrawSettingsScreen(self):
		self.screen.fill((0, 0, 255))

	def __DrawPartyScreen(self):
		pass

	def __DrawShopScreen(self):
		pass

	def __DrawBattleScreen(self):
		pass
