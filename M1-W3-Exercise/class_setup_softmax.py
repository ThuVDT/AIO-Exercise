import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        denominator = torch.sum(exp_x)
        return exp_x/denominator


class softmax_stable(nn.Module):
    def __init__(self):
        super(softmax_stable, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x - torch.max(x))
        denominator = torch.sum(exp_x)
        return exp_x/denominator


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)

data = torch.Tensor([1, 2, 3])
softmax_stable = softmax_stable()
output = softmax_stable(data)
print(output)
