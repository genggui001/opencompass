---
jupyter:
  title: Building Sankey Diagrams Using Hypothetical Data.
  module: matplotlib
  dataset: none
  difficulty: MIDDLE
  idx: 48
  num_steps: 6
  step_types:
    - vis
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
---

Create a basic Sankey diagram with one flow. This flow goes from 'input' to 'output'. The flow is represented by a list of two elements [1, -1]. The first element (1) is the input flow, and the second element (-1) is the output flow. The labels for these flows are also provided in a list ['input', 'output'].
```python
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey
Sankey(flows=[1, -1], labels=['input', 'output']).finish()
plt.show()
```

Create a series of Sankey diagrams by first initializing a Sankey object and then adding flows to it using the 'add' method.
```python
sankey = Sankey(flows=[1, -1], labels=['input', 'output'], orientations=[0, 1])
sankey.add(flows=[1, -1, 0.5, -0.5], labels=['input', 'output', 'input2', 'output2'], pathlengths=[0.5, 0.5, 0.75, 0.75])
sankey.finish()
plt.show()
```

Adjust the orientation of subsequent Sankey diagrams using the 'orientations' parameter in the 'add' method.
```python
sankey = Sankey(flows=[1, -1], labels=['input', 'output'], orientations=[0, 1])
sankey.add(flows=[1, -1, 0.5, -0.5], labels=['input', 'output', 'input2', 'output2'], pathlengths=[0.5, 0.5, 0.75, 0.75], orientations=[0, 1, 0, 1])
sankey.finish()
plt.show()
```

Connect the diagrams by using the 'prior' and 'connect' parameters in the 'add' method. 'prior' is an index to the previous diagram that should be connected, and 'connect' is a tuple where the first value is the output index in the prior diagram and the second value is the input index in the current diagram.
```python
sankey = Sankey(flows=[1, -1], labels=['input', 'output'], orientations=[0, 1])
sankey.add(flows=[1, -1, 0.5, -0.5], labels=['input', 'output', 'input2', 'output2'], pathlengths=[0.5, 0.5, 0.75, 0.75], orientations=[0, 1, 0, 1], prior=0, connect=(1, 0))
sankey.finish()
plt.show()
```

Customize the style of the Sankey diagram by adding a style parameter. In this case, we add the 'facecolor' parameter to change the color of the flows to 'lightgreen'.
```python
sankey = Sankey(flows=[1, -1], labels=['input', 'output'], orientations=[0, 1])
sankey.add(flows=[1, -1, 0.5, -0.5], labels=['input', 'output', 'input2', 'output2'], pathlengths=[0.5, 0.5, 0.75, 0.75], orientations=[0, 1, 0, 1], prior=0, connect=(1, 0), facecolor='lightgreen')
sankey.finish()
plt.show()
```

Add multiple subsequent Sankey diagrams by calling the 'add' method multiple times. Here, we add another Sankey diagram to the previous one with its own flows, labels, path lengths, orientations, prior connection, and face color.
```python
sankey = Sankey(flows=[1, -1], labels=['input', 'output'], orientations=[0, 1])
sankey.add(flows=[1, -1, 0.5, -0.5], labels=['input', 'output', 'input2', 'output2'], pathlengths=[0.5, 0.5, 0.75, 0.75], orientations=[0, 1, 0, 1], prior=0, connect=(1, 0), facecolor='lightgreen')
sankey.add(flows=[1, -0.5, -0.5], labels=['input', 'output1', 'output2'], pathlengths=[0.5, 0.25, 0.25], orientations=[0, 1, -1], prior=1, connect=(1, 0), facecolor='lightblue')
sankey.finish()
plt.show()
```