class Item:
    def __init__(self, name: str):
        self.name = name

    def to_dict(self):
        return {
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(name=data["name"])