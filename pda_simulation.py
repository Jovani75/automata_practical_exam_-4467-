class PDA:
    def __init__(self, cfg):
        self.cfg = cfg

    def simulate(self, input_string):
        return input_string in self.cfg

cfg = ["S->aSb", "S->"]
pda = PDA(cfg)
print(pda.simulate("aaabbb"))
print(pda.simulate("aab"))
