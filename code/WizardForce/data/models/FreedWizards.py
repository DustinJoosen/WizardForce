from data.providers.JsonProvider import JsonProvider


class FreedWizards(JsonProvider):
	def __init__(self):
		self.party_members = []
		self.wizards = []

	@classmethod
	def Load(cls):
		wizards = FreedWizards()
		super().LoadIntoObject(wizards, "wizards.json")

		return wizards
