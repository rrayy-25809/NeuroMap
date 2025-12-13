#include <torch/extension.h>

int x = 0;
int y = 0;

torch::Tensor run_map(torch::Tensor input, Map grid) {
    while (true) {
        Cell cell = grid[x][y];
        
    }
}