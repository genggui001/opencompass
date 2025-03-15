---
jupyter:
  title: An Introduction to Tensor Operations in PyTorch
  dataset: None
  difficulty: Easy
  module: pytorch
  idx: 0
  num_steps: 6
  step_types:
    - exec
    - text
    - text
    - text
    - text
    - text
  modules:
    - pytorch
    - pytorch
    - pytorch
    - pytorch
    - pytorch
    - pytorch
---

Create a tensor of size 5x3, initializing it with random values.
```python
import torch
random_tensor = torch.rand(5, 3)
```

Create a tensor of size 5x3 filled with zeros, and specify that it should be of long type. Print the tensor.
```python
zero_tensor = torch.zeros(5, 3, dtype=torch.long)
print(zero_tensor)
```

Create a tensor directly from data, in this case, a list of two numbers [5.5, 3]. Print the tensor.
```python
data_tensor = torch.tensor([5.5, 3])
print(data_tensor)
```

Reshape a zeros tensor from 4x4 to 2x8 formats. Print the reshaped tensor.
```python
reshaped_tensor = torch.zeros(4, 4)
reshaped_tensor2 = reshaped_tensor.view(-1, 8)
print(reshaped_tensor2)
```

Convert a Torch Tensor to a NumPy Array. Print the array.
```python
torch_tensor = torch.ones(5)
numpy_array = torch_tensor.numpy()
print(numpy_array)
```

Create a tensor of 2x2 ones for gradient computation. Perform an add 2 operation on the tensor. Compute gradients and print it.
```python
gradient_tensor = torch.ones(2, 2, requires_grad=True)
operation_result = gradient_tensor + 2
operation_result.backward(torch.ones(2, 2))
print(gradient_tensor.grad)
```
