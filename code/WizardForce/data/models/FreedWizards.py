from data.providers.JsonProvider import JsonProvider


class FreedWizards(JsonProvider):
	@classmethod
	def Load(cls):
		wizards = FreedWizards()
		super().LoadIntoObject(wizards, "../WizardForce/resources/data/json/wizards.json")

		return wizards
