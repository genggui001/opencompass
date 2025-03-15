---
jupyter:
  title: An Introduction to Tensor Operations in PyTorch
  dataset: None
  difficulty: Easy
  module: pytorch
  idx: 6
  num_steps: 5
  step_types:
    - text
    - text
    - exec
    - text
    - vis
  modules:
    - pytorch
    - pytorch
    - pytorch
    - pytorch
    - pytorch&matplotlib
---


Create a tensor 'a' of size 2x2 with floating point numbers [[1., 2.], [3., 4.]]. Enable gradient tracking for this tensor. Perform operations on tensor 'a'. Add 2 to every element of 'a' to get tensor 'b'. Then, square 'b' and multiply the result by 3 to get tensor 'c'. Finally, calculate the mean of 'c' to get tensor 'out'. Print out.
```python
import torch
a = torch.tensor([[1., 2.], [3., 4.]], requires_grad=True)
b = a + 2
c = b * b * 3
out = c.mean()
print(out)
```

Compute the gradients of tensor 'a' through the computational graph from tensor 'out'. Print the gradients of tensor 'a'. 
```python
out.backward()
print(a.grad)
```

Create another tensor 'x' of size 1x3 with floating point numbers. Again, enable gradient tracking for this tensor. Perform an operation on tensor 'x'. Double the elements of 'x' repeatedly until the Euclidean norm (i.e., length) of 'x' is less than 1000.
```python
x = torch.tensor([3., 2., 1.], requires_grad=True)
y = x * 2
while y.data.norm() < 1000:
    y = y * 2
```

Compute the gradients of tensor 'x' by backpropagating the gradient through the computational graph from tensor 'y'. The argument is a tensor of the same shape as 'y' with values [0.1, 1.0, 0.0001]. Print the gradients of tensor 'x'.
```python
v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
y.backward(v)
print(x.grad)
```

Visualize the gradients of tensors 'a' and 'x' using a scatter plot. For each tensor, plot the tensor values on the x-axis and their gradients on the y-axis.
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.subplot(121)
plt.title('Gradients of a')
plt.plot(a.detach().numpy(), a.grad.detach().numpy(), 'ro')
plt.xlabel('a')
plt.ylabel('da')

plt.subplot(122)
plt.title('Gradients of x')
plt.plot(x.detach().numpy(), x.grad.detach().numpy(), 'bo')
plt.xlabel('x')
plt.ylabel('dx')
plt.show()
```