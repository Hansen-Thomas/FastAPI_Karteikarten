class Tag:
    def __init__(self, id: int = None, value: str = ""):
        self.id = id
        self.value = value

    def __eq__(self, other: object) -> bool:
        if other is None:
            return False
        if not isinstance(other, Tag):
            return False
        return self.value == other.value

    def __repr__(self) -> str:
        return f"Tag(id={self.id}, value={self.value})"

    def __str__(self) -> str:
        return self.value
