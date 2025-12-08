import torch.nn as nn
from . import cell

class Map(nn.Module):
    def __init__(self, grid: list[list[cell.Cell]]):
        super().__init__()
        self.grid = grid

    def forward(self, x):
        r, c = 0, 0   # 시작점 (필요하면 자동 탐색으로 바꿀 수 있음)

        while True:
            module, arrow = self.grid[r][c]

            # 텐서를 모듈에 통과시킨다
            x = module(x)

            # STOP이면 종료
            if arrow.value == (0,0):
                return x

            # 다음 위치 계산
            dr, dc = arrow.value
            r, c = r + dr, c + dc
