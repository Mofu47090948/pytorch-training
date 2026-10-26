import torch

scores = torch.tensor([
    [85, 78],
    [67, 82],
    [92, 88]
])

print(scores)
print(scores.shape)

totals = scores.sum(dim=1)
print(totals)

subject_totals = scores.sum(dim=0)
print(subject_totals)
print(subject_totals.shape)

scores_float = scores.float()
averages = scores_float.mean(dim=0)
print(averages)

subjects_first = scores.permute(1, 0)
print(subjects_first)
print(subjects_first.shape)