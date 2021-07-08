class ButtonEvents:
	screen_manager = None

	@classmethod
	def OpenScreen(cls, screen_code):
		cls.screen_manager.SetScreenCode(screen_code)
		print(f"Opening screen {screen_code}")

	@classmethod
	def CloseGame(cls):
		cls.screen_manager.running = False
		print("Closing game. Thanks for playing!")

	@classmethod
	def ScreenRollBack(cls):
		cls.OpenScreen(cls.screen_manager.screen_history[-2])
		print("Rolling back screen")

	@classmethod
	def TogglePlayMusic(cls):
		settings = cls.screen_manager.data_context.Settings.Load()
		settings.play_music = not settings.play_music

		settings.Save()

		cls.screen_manager.SetScreenCode(cls.screen_manager.screen_code)
		print("play_music is toggled")