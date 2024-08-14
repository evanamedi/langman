from .item import Item

class Language(Item):
    def __init__(self, name: str, keywords=None, standard_library=None):
        super().__init__(name)
        self.keywords = keywords or []
        self.standard_library = standard_library or []
    
    def add_keyword(self, keyword: str):
        if keyword not in self.keywords:
            self.keywords.append(keyword)
    
    def add_library(self, library: str):
        if library not in self.standard_library:
            self.standard_library.append(library)
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
			"keywords": self.keywords,
			"standard_library": self.standard_library
		})
        return data
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
			name=data["name"],
			keywords=data.get("keywords", []),
			standard_library=data.get("standard_library", [])
		)