---
jupyter:
  title: Analyzing a 1D Signal using Fourier Transform and Filters
  module: SciPy
  dataset: None
  difficulty: EASY
  idx: 33
  num_steps: 5
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
  modules: 
    - numpy
    - matplotlib
    - scipy & numpy & matplotlib
    - scipy & matplotlib
    - scipy & matplotlib
---

Generate a 1D signal of 500 data points which is a sine wave. The time variable is created using an array of 500 points from 0-499. Add Gaussian noise to the signal with a standard deviation of 0.2
```python
import numpy as np

n_samples = 500
time = np.arange(n_samples)
signal = np.sin(2 * np.pi * time / n_samples)
noise = 0.2 * np.random.normal(size=n_samples)
signal = signal + noise
```

Use matplotlib to plot the noisy signal.
```python
import matplotlib.pyplot as plt

plt.plot(time, signal)
plt.title('Noisy signal')
plt.show()
```

Apply a Fourier transform to the signal. Plot the Fourier transform of the signal. The frequencies variable is created using a linear space.

```python
from scipy.fft import fft

f_signal = fft(signal)
frequencies = np.linspace(0.0, 1.0/(2.0/n_samples), n_samples//2)
plt.plot(frequencies, 2.0/n_samples * np.abs(f_signal[0:n_samples//2]))
plt.title('Fourier transform')
plt.show()
```

Apply a low-pass Butterworth filter of order 5 to the signal with a cutoff frequency of 0.1. Plot the signal after applying the low-pass filter.

```python
from scipy.signal import butter, lfilter

b, a = butter(5, 0.1, btype='low')
filtered_signal = lfilter(b, a, signal)
plt.plot(time, filtered_signal)
plt.title('Filtered signal')
plt.show()
```

Apply a high-pass Butterworth filter of order 5 to the signal with a cutoff frequency of 0.1. Plot the signal after applying the high-pass filter.
```python
b, a = butter(5, 0.1, btype='high')
filtered_signal = lfilter(b, a, signal)
plt.plot(time, filtered_signal)
plt.title('High-pass filtered signal')
plt.show()
```
