from abc import ABC, abstractmethod

class Tool(ABC):
    @abstractmethod
    def run(self, text: str) -> str:
        pass
