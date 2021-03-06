from Enums import EventType
import pygame

pygame.init()


class EventHandler:
	def __init__(self):
		self.__widgets = []

		# self.is_clicking = False

	def AddWidget(self, widget):
		self.__widgets.append(widget)

	def AddWidgets(self, widgets):
		self.__widgets += widgets

	def GetWidgets(self):
		return self.__widgets

	def Clear(self):
		self.__widgets.clear()

	#loops through the widgets, and calls their InvokeEvent method if needed
	def CheckEvents(self):
		for widget in self.__widgets:
			#if the event is configured to accept OnClick events, and it is happening
			if widget.event_type == EventType.OnClick and self.IsOnClicking(widget):
				widget.OnClick()
			# if the event is configured to accept OnHover events, and it is happening
			elif widget.event_type == EventType.OnHover and self.IsHovering(widget):
				widget.OnHover()
			#if the event is configured to accept both events, check if either one is happening
			elif widget.event_type == EventType.Both:
				if self.IsOnClicking(widget):
					widget.OnClick()
				if self.IsHovering(widget):
					widget.OnHover()

	@staticmethod
	def IsOnClicking(widget):
		if not pygame.mouse.get_pressed()[0]:
			return False

		mouse_pos = pygame.mouse.get_pos()

		x_range = list(range(widget.positions[0], widget.positions[0] + widget.dimensions[0]))
		y_range = list(range(widget.positions[1], widget.positions[1] + widget.dimensions[1]))

		return mouse_pos[0] in x_range and mouse_pos[1] in y_range

	@staticmethod
	def IsHovering(widget):
		mouse_pos = pygame.mouse.get_pos()

		x_range = list(range(widget.positions[0], widget.positions[0] + widget.dimensions[0]))
		y_range = list(range(widget.positions[1], widget.positions[1] + widget.dimensions[1]))

		return mouse_pos[0] in x_range and mouse_pos[1] in y_range
