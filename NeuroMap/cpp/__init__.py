from torch.utils.cpp_extension import load
import os

DIR = os.path.dirname(os.path.abspath(__file__))
# https://github.com/pytorch/vision/issues/2360#issuecomment-883574291
neuromap_cpp = load(
    name="neuromap_cpp",
    sources=[
        os.path.join(DIR, "bind.cpp")
    ],
    verbose=True,
)