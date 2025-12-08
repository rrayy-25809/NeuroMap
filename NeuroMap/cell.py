class Cell:
    def __init__(self, module, arrow):
        self.module = module
        self.arrow = arrow

    def __iter__(self):
        return iter((self.module, self.arrow))