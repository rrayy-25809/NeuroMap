#include <torch/extension.h>
#include "test.cpp"

TORCH_LIBRARY(neuromap_cpp, m) {
    m.def("test", &test);
}