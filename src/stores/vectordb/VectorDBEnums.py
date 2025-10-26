from enum import Enum

class VectorDBEnums(Enum):
    QDRANT = "Qdrant"


class DistanceMethodEnums(Enum):
    COSINE = "cosine"
    DOT = "dot"