---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Tips Dataset
  difficulty: Easy
  module: pandas
  idx: 21
  num_steps: 5
  step_types:
    - exec
    - exec
    - exec
    - exec
    - exec
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
---

File Path: `data/tips.csv`

Load the dataset from the provided path. This dataset is in CSV format.
```python
import pandas as pd
df = pd.read_csv('data/tips.csv')
```

Style the DataFrame 'df' by mapping colors to values. Use a gradient with 'viridis' colormap.
```python
df.style.background_gradient(cmap='viridis')
```

Highlight any null values in the DataFrame 'df' with red color.
```python
df.style.highlight_null(color='red')
```

Define a function named 'highlight_tip' to highlight values greater than 0.5 in the 'tip' column using yellow color.
```python
def highlight_tip(value):
    if value > 0.5:
        return 'background-color: yellow'
    else:
        return ''

df.style.applymap(highlight_tip, subset=['tip'])
```

Display a bar plot for the 'total_bill' column inside the DataFrame 'df'. Use light blue color for the bars.
```python
df.style.bar(subset=['total_bill'], color='lightblue')
```