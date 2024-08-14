from langauge import Language
from program import Program

class Manger:
	def __init__(self):
		self.items = {}

	def add_item(self, item_type: str, name: str) -> None:
		"""
		add a new item (langauge, program, etc...) to the mangaer
		"""
		pass

	def remove_item(self, name: str) -> None:
		"""
		remove an item by name
		"""
		pass

	def get_item(self, name: str) -> Item:
		"""
		retrieve an item by name
		"""
		pass

	def list_items(self) -> list:
		"""
		list all items managed by the manager
		"""
		pass

