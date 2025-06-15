from .base import Tool

class SimpleSummarizer(Tool):
    def run(self, text: str) -> str:
        return text[:100] + "..."
