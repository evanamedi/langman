from .item import Item

class Program(Item):
    def __init__(self, name: str, version: str = "1.0"):
        super().__init__(name)
        self.version = version

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "version": self.version
        })
        return data

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            version=data.get("version", "1.0")
        )