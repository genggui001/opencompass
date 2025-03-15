---
jupyter:
  title: Converting a PyTorch model to TorchScript and comparing results
  dataset: None
  difficulty: Easy
  module: pytorch
  idx: 25
  num_steps: 4
  step_types:
    - exec
    - exec
    - exec
    - exec
  modules:
    - pytorch
    - pytorch
    - pytorch
    - pytorch
---

Create a PyTorch model class. This class should be named MyModel and inherit from nn.Module. Inside the class, define a constructor that initializes a weight parameter as a random tensor. Also define a forward method that returns the product of an input and the weight. Use the following Python code to accomplish this:
```python
import torch
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.weight = nn.Parameter(torch.randn(()))

    def forward(self, input):
        return input * self.weight
```

Instantiate the MyModel class. Assign the new instance to a variable named model: Generate random input data for the model. Use the torch.randn function to create a random tensor, and assign it to a variable named input: Run the model with the input data and print the result:
```python
model = MyModel()
input = torch.randn(())
print(model(input))
```

Convert the PyTorch model to TorchScript. Use the JIT (Just-In-Time) compiler, and assign the result to a variable named scripted_model: Print the code of the scripted model.
```python
scripted_model = torch.jit.script(model)
print(scripted_model.code)
```

Verify that the results of the original model and the TorchScript model are identical. Compare them using the equality operator. First, calculate the results of both models and assign them to the variables original_result and scripted_result: Then, compare these results and print the outcome:
```python
original_result = model(input)
scripted_result = scripted_model(input)
print(original_result == scripted_result)
```
