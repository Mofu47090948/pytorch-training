import torch
from model import MyModel

x = torch.ones((3, 3))
mytensor = torch.full((3, 3), 2.0)

model = MyModel(mytensor, 4.0, 6.0)
result = model(x)

print(result)