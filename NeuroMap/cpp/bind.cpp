#include <pybind11/pybind11.h>
#include <torch/extension.h>
#include "test.cpp"

PYBIND11_MODULE(neuromap_cpp, m) {
    m.def("test", &test, "Test function that multiplies tensor by 2");
}