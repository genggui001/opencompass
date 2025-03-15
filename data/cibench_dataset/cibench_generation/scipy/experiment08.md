---
jupyter:
  title: Statistical Analysis and Visualization of Random Data
  module: SciPy
  dataset: None
  difficulty: NORMAL
  idx: 8
  num_steps: 7
  step_types:
    - num
    - vis
    - vis
    - num
    - num
    - exec
    - exec
  modules: 
    - numpy & scipy
    - numpy & scipy & matplotlib
    - scipy & matplotlib
    - numpy & scipy
    - scipy
    - numpy & scipy
    - scipy
---

Given data = [-0.63,  0.05, -0.05,  1.21,  1.23,  0.86,  0.16, -1.6 , -1.08, -1.08]. Calculate the mode of the data. The result is rounded to two decimal places.
```python
import numpy as np
from scipy import stats

data = np.array([-0.63,  0.05, -0.05,  1.21,  1.23,  0.86,  0.16, -1.6 , -1.08, -1.08])

mode = stats.mode(data)
round(mode.mode, 2)
```

Calculate and plot the Probability Density Function (PDF) of x = np.linspace(0, 1, 100).
```python
import matplotlib.pyplot as plt
x = np.linspace(0, 1, 100)
p = stats.norm.pdf(x, 0, 1)
plt.plot(x, p, 'k', linewidth=2)
plt.show()
```

Calculate and plot the Cumulative Density Function (CDF) of x = np.linspace(0, 1, 100).
```python
p = stats.norm.cdf(x, 0, 1)
plt.plot(x, p, 'k', linewidth=2)
plt.show()
```

Calculate the Percent Point Function (PPF) of [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]. Display the first value of ppf and rounded to two decimal places.
```python
q = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
ppf = stats.norm.ppf(q, 0, 1)

round(ppf[0], 2)
```

Test the normality of the data in first step using the Shapiro-Wilk. Display the p value and rounded to two decimal places.
```python
w, p = stats.shapiro(data)

round(p, 2)
```

Generate another two sets of 1000 random numbers each following a standard normal distribution. Then, calculate the Pearson correlation between the two new sets of data. The result is rounded to two decimal places.
```python
data1 = np.random.randn(1000)
data2 = np.random.randn(1000)

corr, p = stats.pearsonr(data1, data2)

print(f"Correlation: {corr:.2f}, p-value: {p:.2f}")
```

Perform a simple linear regression on the two new sets of data. The result is rounded to two decimal places.
```python
slope, intercept, r_value, p_value, std_err = stats.linregress(data1, data2)

print(f"Slope: {slope:.2f}, Intercept: {intercept:.2f}, R-value: {r_value:.2f}, p-value: {p_value:.2f}, Std Err: {std_err:.2f}")
```