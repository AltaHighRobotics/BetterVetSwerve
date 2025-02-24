class Flag:
    """
    Flags allow for commication between state and subsystems
    """
    def __init__(self, dataType: str, data):
        self.type = dataType
        self.data = data
    
    def getType(self) -> str:
        return self.type
    
    def read(self):
        return self.data
    
    def dismiss(self) -> None:
        del self
