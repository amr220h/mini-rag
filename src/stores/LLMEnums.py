from enum import Enum

class LLMType(Enum):
    OPENAI = "OPENAI"
    COHERE = "COHERE"

class OpenAIEnum(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
