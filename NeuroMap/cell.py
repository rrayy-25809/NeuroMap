from typing import Union
from NeuroMap import Arrow
from torch.nn import Module
from types import FunctionType

class Cell:
    def __init__(self, soma: Union[FunctionType, Module], arrow: Arrow):
        self.soma = soma
        self.arrow = arrow