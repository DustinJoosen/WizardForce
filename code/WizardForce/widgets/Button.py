from widgets.Widget import Widget


class Button(Widget):
	def __init__(self, positions, dimensions, event, event_type, args=None):
		super().__init__(positions, dimensions, event_type)

		#arguments may need to be passed along to the event
		self.event = event
		self.args = args

	def OnClick(self):
		if self.args is None:
			self.event()
		else:
			self.event(self.args)
