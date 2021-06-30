from data.providers.SqliteProvider import SqliteProvider
from data.models.Move import MoveSet


class Level(SqliteProvider):
	def __init__(self):
		self.Id = 0
		self.LevelCode = None
		self.CoinsRewarded = 0

	def InitProvider(self):
		super().__init__("Levels", Level)

	def GetById(self, id):
		level = super().GetById(id)
		foes = Level.GetFoes(level.Id)

		setattr(level, "Foes", foes)
		return level

	def GetByCode(self, level_code):
		level = super().GetByQuery(f"SELECT * FROM Levels WHERE LevelCode = '{level_code}'")[0]
		foes = Level.GetFoes(level.Id)

		setattr(level, "Foes", foes)
		return level

	@classmethod
	def GetFoes(cls, level_id):
		lf = LevelFoe()
		lf.InitProvider()

		output = []

		foes = lf.GetAll()
		for foe in foes:
			if foe.LevelId == level_id:
				output.append(foe)

		return output


class LevelFoe(SqliteProvider):
	def __init__(self):
		self.Id = 0
		self.LevelId = 0
		self.DefaultMoveSetId = 0
		self.HP = 0
		self.ImageName = None

	def InitProvider(self):
		super().__init__("LevelFoes", LevelFoe)

	def GetById(self, id):
		foe = super().GetById(id)
		moves = LevelFoe.GetMove(foe.DefaultMoveSetId)

		setattr(foe, "Moves", moves)
		return foe

	def GetAll(self):
		foes = super().GetAll()

		for foe in foes:
			moves = LevelFoe.GetMove(foe.DefaultMoveSetId)
			setattr(foe, "Moves", moves)

		return foes

	@classmethod
	def GetMove(cls, moveSetId):
		ms = MoveSet()
		ms.InitProvider()

		return ms.GetById(moveSetId)
