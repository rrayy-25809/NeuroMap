from enum import Enum
import random

class Arrow(Enum):
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    UP = (-1, 0)
    STOP = (0, 0)

    def __add__(self, other:Arrow) -> Arrow:
        dr1, dc1 = self.value
        dr2, dc2 = other.value
        return Arrow((dr1 + dr2, dc1 + dc2))
    
    def __mul__(self, factor: int) -> Arrow:
        dr, dc = self.value
        return Arrow((dr * factor, dc * factor))
    
    def __or__(self, value: Arrow) -> Arrow:
        return random.choice([self, value]) # 랜덤으로 둘 중 하나 선택