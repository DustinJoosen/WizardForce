from widgets.Widget import Widget


class Button(Widget):
	def __init__(self, positions, dimensions, event_type, event, args=None, image=None):
		super().__init__(positions, dimensions, event_type, image)

		#arguments may need to be passed along to the event
		self.event = event
		self.args = args

	def OnClick(self):
		if self.args is None:
			self.event()
		else:
			self.event(self.args)
