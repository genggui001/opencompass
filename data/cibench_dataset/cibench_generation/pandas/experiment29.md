---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: None
  difficulty: Easy
  module: pandas
  idx: 29
  num_steps: 4
  step_types:
    - exec
    - exec
    - exec
    - vis
  modules:
    - pandas
    - pandas
    - pandas
    - pandas&matplotlib
---

Create a DataFrame with 10000 rows and 4 columns filled with random numbers generated.
```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10000, 4))
```

Calculate the sparsity of the DataFrame. Sparsity is calculated as 1.0 minus the ratio of non-zero elements to the total number of elements. Keep to 2 decimal places.

```python
sparsity = 1.0 - ( np.count_nonzero(df) / float(df.size) )
round(sparsity,2)
```

Convert the DataFrame to a SparseDataFrame using pandas' astype function with the SparseDtype parameter set to "float" and fill_value set to np.nan.
Calculate the sparsity of the SparseDataFrame using the density attribute of the sparse property. Keep to 2 decimal places.
```python
sdf = df.astype(pd.SparseDtype("float", np.nan))
sparsity_sdf = 1.0 - ( sdf.sparse.density )
round(sparsity_sdf,2)
```


Visualize the non-empty data in the SparseDataFrame using matplotlib's spy function.
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.spy(sdf, markersize=0.5)
plt.show()
```
