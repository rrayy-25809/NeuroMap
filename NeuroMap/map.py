import torch.nn as nn
from NeuroMap import Cell

class Map(nn.Module):
    def __init__(self, grid: list[list[Cell]]):
        super().__init__()
        self.grid = grid

    def forward(self, x):
        r, c = 0, 0   # 시작점 (필요하면 자동 탐색으로 바꿀 수 있음)

        while True:
            cell = self.grid[r][c]
            soma = cell.soma
            arrow = cell.arrow

            # 텐서를 모듈에 통과시킨다
            x = soma(x)

            # STOP이면 종료
            if arrow.value == (0,0):
                return x

            # 다음 위치 계산
            dr, dc = arrow.value
            r, c = r + dr, c + dc
