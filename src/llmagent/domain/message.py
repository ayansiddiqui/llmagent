from dataclasses import dataclass

@dataclass
class Message:
    user: str
    content: str
