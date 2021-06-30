from data.providers.SqliteProvider import SqliteProvider


class Move(SqliteProvider):
	def __init__(self):
		self.Id = 0
		self.Name = None
		self.MagicType = None
		self.Damage = 0
		self.RechargeTime = 0
		self.IsExclusive = False

	def InitProvider(self):
		super().__init__("MoveView", Move)


class MoveSet(SqliteProvider):
	def __init__(self):
		self.Id = 0
		self.Move1Id = 0
		self.Move2Id = 0
		self.Move3Id = 0
		self.Move4Id = 0

	def InitProvider(self):
		super().__init__("MoveSets", MoveSet)

	def GetById(self, id):
		moveset = super().GetById(id)
		return MoveSet.GetMoves(moveset)

	def GetAll(self):
		movesets = super().GetAll()
		output = []

		for moveset in movesets:
			moves = MoveSet.GetMoves(moveset)
			output.append(moves)

		return output

	@classmethod
	def GetMoves(cls, moveset):
		output = []

		m = Move()
		m.InitProvider()

		moves = m.GetAll()

		for move in moves:
			if move.Id in [moveset.Move1Id, moveset.Move2Id, moveset.Move3Id, moveset.Move4Id]:
				output.append(move)

		return output
