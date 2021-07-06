from data.providers.SqliteProvider import SqliteProvider
from data.models.Move import MoveSet
from data.models.FreedWizards import FreedWizards


class Wizard(SqliteProvider):
	def __init__(self):
		self.Id = 0
		self.Name = None
		self.OriginLevel = 0
		self.ImageName = None
		self.MagicType = None
		self.DefaultMoveSetId = 0

	def InitProvider(self):
		super().__init__("WizardView", Wizard)

	def GetById(self, id):
		wizard = super().GetById(id)
		moves = Wizard.GetMove(wizard.DefaultMoveSetId)

		setattr(wizard, "Moves", moves)
		return wizard

	def GetAll(self):
		wizards = super().GetAll()

		for wizard in wizards:
			moves = Wizard.GetMove(wizard.DefaultMoveSetId)
			setattr(wizard, "Moves", moves)

		return wizards

	def GetPartyWizards(self):
		freed_wizards = FreedWizards.Load()

		query = "SELECT * FROM WizardView WHERE "
		for i, wizardId in enumerate(freed_wizards.party_members):
			if i == 0:
				query = f"{query} Id = {wizardId}"
			else:
				query = f"{query} OR Id = {wizardId}"

		wizards = self.GetByQuery(query)

		#load the relative wizard data in the json file into the objects
		for wizard in wizards:
			for freed_wizard in freed_wizards.wizards:
				if wizard.Id == freed_wizard["Id"]:
					relative_wizard_data = freed_wizard

			if relative_wizard_data is not None:
				setattr(wizard, "relative_data", relative_wizard_data)

		return wizards

	@classmethod
	def GetMove(cls, moveSetId):
		ms = MoveSet()
		ms.InitProvider()

		return ms.GetById(moveSetId)
