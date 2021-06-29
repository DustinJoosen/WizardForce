from Enums import EventType


class Widget:
	def __init__(self, positions, dimensions, event_type):
		self.positions = positions
		self.dimensions = dimensions
		self.event_type = event_type

	#execute the correct method of the widget, depending on the event_type
	def InvokeEvent(self, event_type):
		if event_type == EventType.OnClick:
			self.OnClick()
		elif event_type == EventType.OnHover:
			self.OnHover()
		elif event_type == EventType.Both:
			self.OnClick()
			self.OnHover()

	def OnClick(self):
		print(f"Clicked on widget at location: {self.positions}")

	def OnHover(self):
		print(f"Hovered above widget at location: {self.positions}")
