import numpy as np
import torch

data = np.array([
    [[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
    [[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
    [[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]
])

scores = torch.tensor(data, dtype=torch.float32)

subjects_first = scores.permute(2, 0, 1)

student_totals = subjects_first.sum(dim=0)
class_averages = student_totals.mean(dim=1)
class_averages_manual = (
    student_totals.sum(dim=1) / student_totals.shape[1]
)

print(class_averages)
print(class_averages_manual)
print(torch.allclose(class_averages, class_averages_manual))