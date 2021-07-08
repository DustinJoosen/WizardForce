from Enums import EventType
import pygame


class Widget:
	def __init__(self, positions, dimensions, event_type, image=None):
		self.positions = positions
		self.dimensions = dimensions
		self.image = image
		self.event_type = event_type

		self.__draw_tuple = tuple(self.positions + self.dimensions)

	def Display(self, screen):
		if self.image is not None:
			screen.blit(self.image, (self.positions[0], self.positions[1]))
		else:
			pygame.draw.rect(screen, (0, 0, 0), self.__draw_tuple)

	def OnClick(self):
		print(f"Clicked on widget at location: {self.positions}")

	def OnHover(self):
		print(f"Hovered above widget at location: {self.positions}")
