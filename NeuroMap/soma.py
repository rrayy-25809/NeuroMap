from .cpp import neuromap_cpp

class Soma:
    def __init__(self):
        pass

    def __call__(self, x):
        return self.forward(x)
    
    def forward(self, x):
        return x

class Test(Soma): # 상속 및 Cpp 테스트 용
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return neuromap_cpp.test(x) # type: ignore
    