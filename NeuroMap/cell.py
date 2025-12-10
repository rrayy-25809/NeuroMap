from .soma import Soma
from typing import Union
from .arrow import Arrow
from torch.nn import Module
from types import FunctionType

class Cell(Module):
    def __init__(self, soma: Union[FunctionType, Module, Soma], arrow: Union[Arrow, tuple[Arrow]]):
        super().__init__()
        self.soma = soma
        self.arrow = arrow

    def forward(self, x):
        return self.soma(x), self.arrow