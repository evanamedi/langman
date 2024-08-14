from item import Item

class Language(Item):
	def __init__(self, name: str):
		super().__init__(name)

	def specific_language_method(self):
		"""
		placeholder for any langauge-specific funtionality
		"""
		pass