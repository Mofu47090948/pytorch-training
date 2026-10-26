import torch
from torch import nn

class MyModel(nn.Module):
    def __init__(self, mytensor, elem_add, elem_multiply):
        super().__init__()
        self.mytensor = mytensor
        self.elem_add = elem_add
        self.elem_multiply = elem_multiply
    def forward(self, x):
        x = x + self.mytensor
        x = x + self.elem_add
        x = x * self.elem_multiply
        return x