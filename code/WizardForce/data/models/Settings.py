from data.providers.JsonProvider import JsonProvider


class Settings(JsonProvider):
	def __init__(self):
		self.play_music = None
		self.music_volume = 0
		self.flash_red_on_damage = None

	@classmethod
	def Load(cls):
		settings = Settings()
		super().LoadIntoObject(settings, "settings.json")

		return settings
