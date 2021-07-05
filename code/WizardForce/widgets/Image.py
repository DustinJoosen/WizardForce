from Enums import EventType
from widgets.Widget import Widget
import pygame


class Image(Widget):
	def __init__(self, positions, image):
		super().__init__(positions, [0, 0], EventType.Neither, image=image)
