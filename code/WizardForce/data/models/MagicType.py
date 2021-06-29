from data.providers.SqliteProvider import SqliteProvider


class MagicType(SqliteProvider):
	def __init__(self):
		self.Id = 0
		self.Name = None

	def InitProvider(self):
		super().__init__("MagicTypes", MagicType)

