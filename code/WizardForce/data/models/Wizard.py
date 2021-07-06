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

	#returns a list of wizard objects, from the wizards.json file in the party_members list
	def GetPartyWizards(self):
		freed_wizards = FreedWizards.Load()

		#start constructing a SQL query, to get all wizards in the party_members
		query = "SELECT * FROM WizardView WHERE "
		for i, wizardId in enumerate(freed_wizards.party_members):
			if i == 0:
				query = f"{query} Id = {wizardId}"
			else:
				query = f"{query} OR Id = {wizardId}"

		#convert the query into a list of wizard objects
		wizards = self.GetByQuery(query)

		#load the relative wizard data in the json file into the objects
		self.__LoadRelativeData(wizards, freed_wizards.wizards)

		return wizards

	#returns the exact opposite of the above method. It returns the wizards that are freed, yet not in your party
	def GetNonPartyWizards(self):
		freed_wizards = FreedWizards.Load()

		#filter out the wizards that are in your party
		non_party_wizards = [w for w in freed_wizards.wizards if w["Id"] not in freed_wizards.party_members]

		#start constructing the query
		query = "SELECT * FROM WizardView WHERE "
		for i, npw in enumerate(non_party_wizards):
			if i == 0:
				query = f"{query} Id = {npw['Id']}"
			else:
				query = f"{query} OR Id = {npw['Id']}"

		wizards = self.GetByQuery(query)
		self.__LoadRelativeData(wizards, freed_wizards.wizards)

		return wizards

	@staticmethod
	def __LoadRelativeData(wizards, relative_data):
		relative_wizard_data = None

		for wizard in wizards:
			for freed_wizard in relative_data:
				if wizard.Id == freed_wizard["Id"]:
					relative_wizard_data = freed_wizard

			if relative_wizard_data is not None:
				setattr(wizard, "relative_data", relative_wizard_data)

	@classmethod
	def GetMove(cls, moveSetId):
		ms = MoveSet()
		ms.InitProvider()

		return ms.GetById(moveSetId)
