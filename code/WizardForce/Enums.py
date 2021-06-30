from enum import Enum


class EventType(Enum):
	OnClick = 0
	OnHover = 1
	Both = 2


class ScreenCode(Enum):
	IS_StartScreen = 0
	IS_MainScreen = 1
	IS_SettingsScreen = 2
	IS_PartyScreen = 3
	IS_ShopScreen = 4
	IS_BattleScreen = 5
