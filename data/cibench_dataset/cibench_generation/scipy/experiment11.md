---
jupyter:
  title: Exploring Special Functions with scipy.special in Python
  module: SciPy
  dataset: None
  difficulty: EASY
  idx: 11
  num_steps: 9
  step_types:
    - num
    - num
    - num
    - num
    - num
    - num
    - num
    - num
    - vis
  modules: 
    - scipy
    - scipy
    - scipy
    - scipy
    - scipy
    - scipy
    - scipy
    - scipy
    - numpy & scipy & matplotlib
---

Compute the factorial of 5. Display the result and rounded to two decimal places.
```python
from scipy import special
round(special.factorial(5), 2)
```

Compute the binomial coefficient of 5 and 3. Display the result and rounded to two decimal places.
```python
round(special.comb(5, 3), 2)
```

Evaluate the gamma function at 0.5. Display the result and rounded to two decimal places.
```python
round(special.gamma(0.5), 2)
```

Evaluate the error function at 0.5. Display the result and rounded to two decimal places.
```python
round(special.erf(0.5), 2)
```

Evaluate the Bessel function of the first kind of integer order 0 at 1. Display the result and rounded to two decimal places.
```python
round(special.jv(0, 1), 2)
```

Evaluate the exponential integral function at 1. Display the result and rounded to two decimal places.
```python
round(special.expi(1), 2)
```

Evaluate the spherical Bessel function of the first kind at 1 for integer order 0. Display the result and rounded to two decimal places.
```python
round(special.spherical_jn(0, 1), 2)
```

Compute the elliptic integral of the second kind (E) at 0.5. Display the result and rounded to two decimal places.
```python
round(special.ellipe(0.5), 2)
```

Plot the Legendre polynomials of degree 0, 1, 2, and 3 from -1 to 1. Include a legend and grid for clarity.
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1, 1, 500)

for n in range(4):
    Pn = special.legendre(n)
    y = Pn(x)
    plt.plot(x, y, label='$P_{%s}(x)$' % n)

plt.legend()
plt.grid()
plt.show()
```