from data.providers.JsonProvider import JsonProvider


class Settings(JsonProvider):
	@classmethod
	def Load(cls):
		settings = Settings()
		super().LoadIntoObject(settings, "../WizardForce/resources/data/json/settings.json")

		return settings
