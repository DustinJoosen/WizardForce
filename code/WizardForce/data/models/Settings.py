from data.providers.JsonProvider import JsonProvider


class Settings(JsonProvider):
	@classmethod
	def Load(cls):
		settings = Settings()
		super().LoadIntoObject(settings, "settings.json")

		return settings
