from data.providers.JsonProvider import JsonProvider


class FreedWizards(JsonProvider):
	@classmethod
	def Load(cls):
		wizards = FreedWizards()
		super().LoadIntoObject(wizards, "wizards.json")

		return wizards
