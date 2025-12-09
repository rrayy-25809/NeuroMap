from NeuroMap import Map, Cell, Arrow
from torch.nn import Linear
from torch.nn import Softmax

L1 = Linear(10, 20)
L2 = Linear(20, 30)
SM = Softmax(dim=1)
L3 = Linear(30, 5)

model = Map([
    [Cell(L1, Arrow.RIGHT), Cell(L2, Arrow.DOWN)],
    [Cell(L3, Arrow.STOP),  Cell(SM, Arrow.LEFT)]
    ])

