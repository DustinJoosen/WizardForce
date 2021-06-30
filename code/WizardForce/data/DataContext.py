from data.models.Level import Level
from data.models.Level import LevelFoe
from data.models.Move import Move
from data.models.Move import MoveSet
from data.models.ShopItem import ShopItem
from data.models.Wizard import Wizard
from data.models.Settings import Settings
from data.models.Progress import Progress
from data.models.FreedWizards import FreedWizards


class DataContext:
	def __init__(self):
		self.Level = Level()
		self.LevelFoe = LevelFoe()
		self.Move = Move()
		self.MoveSet = MoveSet()
		self.ShopItem = ShopItem()
		self.Wizard = Wizard()

		self.FreedWizards = FreedWizards.Load()
		self.Settings = Settings.Load()
		self.Progress = Progress.Load()

	def InitProviders(self):
		self.Level.InitProvider()
		self.LevelFoe.InitProvider()
		self.Move.InitProvider()
		self.MoveSet.InitProvider()
		self.ShopItem.InitProvider()
		self.Wizard.InitProvider()
