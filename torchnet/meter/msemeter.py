import math
from . import meter
import torch


class MSEMeter(meter.Meter):
    def __init__(self, root=False):
        self.reset()
        self.root = root

    def reset(self):
        self.n = 0
        self.sesum = 0.0

    def add(self, output, target):
        if not torch.is_tensor(output) and not torch.is_tensor(target):
            output = torch.from_numpy(output)
            target = torch.from_numpy(target)
        self.n += output.numel()
        self.sesum += torch.sum((output - target) ** 2)

    def value(self):
        mse = self.sesum / max(1, self.n)
        return math.sqrt(mse) if self.root else mse