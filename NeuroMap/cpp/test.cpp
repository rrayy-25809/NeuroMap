#include <torch/extension.h>

torch::Tensor test(torch::Tensor input) {
    // Example operation: just return the input tensor multiplied by 2
    return input * 2;
}