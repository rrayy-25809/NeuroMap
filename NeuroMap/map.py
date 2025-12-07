import torch.nn as nn

class Map(nn.Module):
    def __init__(self, grid):
        super().__init__()
        self.grid = grid

        # 모듈을 nn.Module로 등록해야 PyTorch에서 파라미터 추적 가능
        for row in grid:
            for cell in row:
                module, _ = cell
                if isinstance(module, nn.Module):
                    self.add_module(str(id(module)), module)

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
