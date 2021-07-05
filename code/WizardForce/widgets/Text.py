from widgets.Widget import Widget
import pygame


class Text(Widget):
	def __init__(self, text, positions, event_type, event, args=None, color=(255, 255, 255), fontsize=30):
		#arguments may need to be passed along to the event
		self.event = event
		self.args = args

		#set the font and surface
		self.__font = pygame.font.SysFont('Cambria', fontsize)
		self.text_surface = self.__font.render(text, False, color)

		super().__init__(positions, list(self.__font.size(text)), event_type)

	def Display(self, screen):
		screen.blit(self.text_surface, (self.positions[0], self.positions[1]))

	def OnHover(self):
		if self.args is None:
			self.event()
		else:
			self.event(self.args)
