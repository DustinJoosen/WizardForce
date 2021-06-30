from data.providers.SqliteProvider import SqliteProvider
from data.models.Move import MoveSet


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

	@classmethod
	def GetMove(cls, moveSetId):
		ms = MoveSet()
		ms.InitProvider()

		return ms.GetById(moveSetId)
