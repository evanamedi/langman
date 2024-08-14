from manager import Manger

class DataHandler:
	def __init__(self, data_file: str):
		self.data_file = data_file

	def load_data(self) -> Manager:
		"""
		load the data from a file and return a Manager instance
		"""
		pass

	def save_data(self, manager: Manager) -> None:
		"""
		save the current state of the manager to a file
		"""
		