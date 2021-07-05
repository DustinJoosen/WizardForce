from Enums import ScreenCode, EventType
from events.EventHandler import EventHandler
from widgets.Button import Button
from widgets.Text import Text
from widgets.Image import Image as ImageW
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

		self.image_root = "../WizardForce/resources/sprites"

		#record the previous screencodes
		self.screen_history = []

		#create two often reucurring sprites
		self.images["generic_button_sprite"] = pygame.image.load(f"{self.image_root}/buttons/generic.png")
		self.images["generic_bg_sprite"] = pygame.image.load(f"{self.image_root}/backgrounds/generic_bg.jpg")

		#init the screen
		self.screen_code = ScreenCode.IS_StartScreen
		self.SetScreenCode(self.screen_code)

	def SetScreenCode(self, screen_code):
		self.screen_code = screen_code
		self.event_handler.Clear()

		self.screen_history.append(screen_code)

		if self.screen_code == ScreenCode.IS_StartScreen:
			self.__InitStartScreen()
		elif self.screen_code == ScreenCode.IS_MainScreen:
			self.__InitMainScreen()
		elif self.screen_code == ScreenCode.IS_SettingsScreen:
			self.__InitSettingsScreen()
		elif self.screen_code == ScreenCode.IS_PartyScreen:
			self.__InitPartyScreen()
		elif self.screen_code == ScreenCode.IS_ShopScreen:
			self.__InitShopScreen()
		elif self.screen_code == ScreenCode.IS_BattleScreen:
			self.__InitBattleScreen()

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
		self.images["bg_sprite"] = pygame.image.load(f"{self.image_root}/backgrounds/mainscreen_bg.jpg")
		self.images["header_sprite"] = pygame.image.load(f"{self.image_root}/gametitle_header.png")
		self.images["mainmenu_option"] = pygame.image.load(f"{self.image_root}/buttons/mainmenu_option.png")

		sp_button = Button([245, 195], [310, 90], EventType.OnClick, ButtonEvents.OpenScreen,
						args=ScreenCode.IS_MainScreen, image=self.images["mainmenu_option"])
		op_button = Button([245, 290], [310, 90], EventType.OnClick, ButtonEvents.OpenScreen,
						args=ScreenCode.IS_SettingsScreen, image=self.images["mainmenu_option"])
		ex_button = Button([245, 385], [310, 90], EventType.OnClick, ButtonEvents.CloseGame,
						image=self.images["mainmenu_option"])

		sp_text = Text("Singleplayer", [310, 220], EventType.Neither, None)
		op_text = Text("Settings", [350, 315], EventType.Neither, None)
		ex_text = Text("Exit", [385, 410], EventType.Neither, None)

		self.event_handler.AddWidgets([sp_button, op_button, ex_button, sp_text, op_text, ex_text])

	def __InitMainScreen(self):
		self.images["mainscreen_btn_sprite"] = pygame.image.load(f"{self.image_root}/buttons/mainscreen_button.png")

		settings_button = Button([640, 100], [140, 60], EventType.OnClick, ButtonEvents.OpenScreen,
							args=ScreenCode.IS_SettingsScreen, image=self.images["mainscreen_btn_sprite"])
		party_button = Button([640, 170], [140, 60], EventType.OnClick, ButtonEvents.OpenScreen,
							args=ScreenCode.IS_PartyScreen, image=self.images["mainscreen_btn_sprite"])
		shop_button = Button([640, 240], [140, 60], EventType.OnClick, ButtonEvents.OpenScreen,
							args=ScreenCode.IS_ShopScreen, image=self.images["mainscreen_btn_sprite"])
		exit_button = Button([640, 310], [140, 60], EventType.OnClick, ButtonEvents.CloseGame,
							image=self.images["mainscreen_btn_sprite"])

		op_text = Text("Settings", [650, 110], EventType.Neither, None)
		pa_text = Text("Party", [670, 180], EventType.Neither, None)
		so_text = Text("Shop", [675, 250], EventType.Neither, None)
		ex_text = Text("Exit", [680, 320], EventType.Neither, None)

		map_image = ImageW([35, 60], pygame.image.load(f"{self.image_root}/map.png"))

		self.event_handler.AddWidgets([map_image, settings_button, party_button, shop_button, exit_button])
		self.event_handler.AddWidgets([op_text, pa_text, so_text, ex_text])

	def __InitSettingsScreen(self):
		back_text = Text("Back", [10, 10], EventType.Neither, None)
		back_button = Button([0, 0], [200, 120], EventType.OnClick, ButtonEvents.ScreenRollBack,
						image=self.images["generic_button_sprite"])

		self.event_handler.AddWidgets([back_button, back_text])

	def __InitPartyScreen(self):
		party_wizards = self.data_context.Wizard.GetPartyWizards()
		wizard_box_image = pygame.image.load(f"{self.image_root}/partyscreen_wizard_box.png")

		idx = 0
		for row in range(2):
			for col in range(2):
				wizard = party_wizards[idx]

				img = pygame.image.load(f"{self.image_root}/wizards/{wizard.ImageName}")
				img = pygame.transform.scale(img, (200, 200))

				wizard_image = ImageW([row * 270 + 80, col * 250 + 30], img)
				wizard_box = ImageW([(row * 270 + 30), (col * 250 + 30)], wizard_box_image)
				wizard_name_text = Text(wizard.Name, [row * 270 + 90, col * 250 + 200],	EventType.Neither, None,
									color=(0, 0, 0), fontsize=20)
				wizard_lvl_text = Text(f"Level: {wizard.OriginLevel}", [row * 270 + 90, col * 250 + 225],
									EventType.Neither, None, color=(0, 0, 0), fontsize=20)

				self.event_handler.AddWidgets([wizard_image, wizard_box, wizard_name_text, wizard_lvl_text])
				idx += 1

		back_text = Text("Back", [640, 440], EventType.Neither, None)
		back_button = Button([580, 400], [200, 120], EventType.OnClick, ButtonEvents.ScreenRollBack,
						image=self.images["generic_button_sprite"])

		self.event_handler.AddWidgets([back_button, back_text])

	def __InitShopScreen(self):
		back_text = Text("Back", [10, 10], EventType.Neither, None)
		back_button = Button([0, 0], [200, 120], EventType.OnClick, ButtonEvents.ScreenRollBack,
						image=self.images["generic_button_sprite"])

		shop_item_texts = []
		shop_items = self.data_context.ShopItem.GetAll()
		for i, shop_item in enumerate(shop_items):
			t = f"{shop_item.Name} - {shop_item.Price}"
			shop_item_texts.append(Text(t, [200, 10+i*60], EventType.Neither, None))

		self.event_handler.AddWidgets([back_button, back_text])
		self.event_handler.AddWidgets(shop_item_texts)

	def __InitBattleScreen(self):
		pass

	#DrawMethods draw the images and objects onto the screen
	def __DrawStartScreen(self):
		self.screen.blit(self.images["bg_sprite"], (0, 0))
		self.screen.blit(self.images["header_sprite"], (117, 40))

		for widget in self.event_handler.GetWidgets():
			widget.Display(self.screen)

	def __DrawMainScreen(self):
		self.screen.blit(self.images["generic_bg_sprite"], (0, 0))

		for widget in self.event_handler.GetWidgets():
			widget.Display(self.screen)

	def __DrawSettingsScreen(self):
		self.screen.blit(self.images["generic_bg_sprite"], (0, 0))

		for widget in self.event_handler.GetWidgets():
			widget.Display(self.screen)

	def __DrawPartyScreen(self):
		self.screen.blit(self.images["generic_bg_sprite"], (0, 0))

		for widget in self.event_handler.GetWidgets():
			widget.Display(self.screen)

	def __DrawShopScreen(self):
		self.screen.blit(self.images["generic_bg_sprite"], (0, 0))

		for widget in self.event_handler.GetWidgets():
			widget.Display(self.screen)

	def __DrawBattleScreen(self):
		pass
