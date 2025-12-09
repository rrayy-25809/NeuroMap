from typing import Union
from .arrow import Arrow
from torch.nn import Module
from torch import Tensor
from types import FunctionType

class Cell(Module):
    def __init__(self, soma: Union[FunctionType, Module], arrow: Arrow):
        super().__init__()
        self.soma = soma
        self.arrow = arrow

    def forward(self, x):
        return self.soma(x), self.arrow