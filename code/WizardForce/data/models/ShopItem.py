from data.providers.SqliteProvider import SqliteProvider


class ShopItem(SqliteProvider):
	def __init__(self):
		self.Id = 0
		self.Name = None
		self.Price = 0
		self.Stock = 0
		self.ImageName = None

	def InitProvider(self):
		super().__init__("ShopItems", ShopItem)

