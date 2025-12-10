from torch.utils.cpp_extension import load
import os
import torch

# 중요!!!
torch_lib_path = os.path.join(os.path.dirname(torch.__file__), "lib")
os.add_dll_directory(torch_lib_path)

DIR = os.path.dirname(os.path.abspath(__file__))

neuromap_cpp = load(
    name="neuromap_cpp",
    sources=[
        os.path.join(DIR, "bind.cpp"),
        # os.path.join(DIR, "test.cpp"),
    ],
    verbose=True,
)