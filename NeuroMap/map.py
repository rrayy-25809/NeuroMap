import torch.nn as nn
from .cell import Cell

class Map(nn.Module):
    def __init__(self, grid: list[list[Cell]]):
        super().__init__()
        
        self.grid = nn.ModuleList()

        for row in grid:
            row_module_list = nn.ModuleList()
            for cell in row:
                row_module_list.append(cell)
            self.grid.append(row_module_list)

    def forward(self, x):
        r, c = 0, 0   # 시작점 (필요하면 자동 탐색으로 바꿀 수 있음)

        while True:
            # print(f"위치 ({r}, {c}), 받은 텐서 크기: {x.shape}")
            cell:Cell = self.grid[r][c] # type: ignore

            x, arrow = cell(x) # 텐서를 모듈에 통과시킨다

            # STOP이면 값
            if arrow.value == (0,0):
                return x

            # 다음 위치 계산
            dr, dc = arrow.value
            r, c = r + dr, c + dc
