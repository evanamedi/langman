class Item:
	def __init__(self, name: str):
		self.name = name
		self.keywords = {}

	def add_keyword(self, keyword: str, description: str) -> None:
		"""
		add a keyword with a description to the item
		"""
		pass

	def remove_keyword(self, keyword: str) -> None:
		"""
		remove a keyword from the item
		"""
		pass

	def get_description(self, keyword: str) -> str:
		"""
		retrieve the description of a keyword
		"""
		pass

	def list_keywords(self) -> list:
		"""
		list all keywords associated with the item
		"""
		pass

	