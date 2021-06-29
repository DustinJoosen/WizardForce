from data.providers.JsonProvider import JsonProvider


class Progress(JsonProvider):
	@classmethod
	def Load(cls):
		progress = Progress()
		super().LoadIntoObject(progress, "../WizardForce/resources/data/json/progress.json")

		return progress
