from .item import Item

class Program(Item):
	def __init__(self, name: str):
		super().__init__(name)

	def specific_program_method(self):
		"""
		placeholder for any program-specific functionality
		"""
		pass