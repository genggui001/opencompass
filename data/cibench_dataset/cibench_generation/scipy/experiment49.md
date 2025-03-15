---
jupyter:
  title: Fourier Transform for Signal Processing
  module: SciPy
  dataset: none
  difficulty: MIDDLE
  idx: 49
  num_steps: 6
  step_types:
    - vis
    - vis
    - vis
    - vis 
    - vis
    - vis 
  modules: 
    - numpy & matplotlib & scipy
    - numpy & matplotlib & scipy
    - matplotlib & scipy
    - matplotlib & scipy
    - matplotlib & scipy
    - matplotlib & scipy
---

Create a time vector 't' from 0 to 1 with an interval of 1/150 (sample frequency of 150Hz). Then, create a sinusoidal signal 'y' with a frequency of 5Hz using this time vector. Plot the original signal.
```python
import numpy as np
import matplotlib.pyplot as plt
Fs = 150.0  # sample frequency
Ts = 1.0/Fs  # sample interval
t = np.arange(0,1,Ts)  # time vector
ff = 5  # frequency of the signal
y = np.sin(2*np.pi*ff*t)

plt.plot(t, y, 'k')
plt.title('Original signal')
plt.show()
```

Compute the discrete Fourier Transform of the sinusoidal signal 'y' and normalize it. Extract half of the Fourier Transform to eliminate the mirrored part of the spectrum. Plot the frequency domain representation of the original signal.
```python
from scipy.fftpack import fft, ifft
n = len(y)  # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T  # two sides frequency range
frq = frq[range(n//2)]  # one side frequency range
Y = fft(y)/n  # fft computing and normalization
Y = Y[range(n//2)]
plt.plot(frq,abs(Y),'r')  
plt.title('Frequency domain of the signal')
plt.show()
```

Add random noise with 0.5 multiple standard randn to the original signal 'y' to simulate a real-world noisy signal. Plot the noisy signal.
```python
y_noisy = y + 0.5*np.random.randn(len(t))
plt.plot(t, y_noisy, 'k')
plt.title('Noisy signal')
plt.show()
```

Compute the discrete Fourier Transform of the noisy signal 'y_noisy' and normalize it. Extract half of the Fourier Transform to eliminate the mirrored part of the spectrum. Plot the frequency domain representation of the noisy signal. Plot the frequency domain of nosiy signal.
```python
Y_noisy = fft(y_noisy)/n  # fft computing and normalization
Y_noisy = Y_noisy[range(n//2)]
plt.plot(frq,abs(Y_noisy),'r')  
plt.title('Frequency domain of the noisy signal')
plt.show()
```


Apply the inverse discrete Fourier Transform to the Fourier Transform of the noisy signal. Plot the constructed signal.
```python
y_reconstructed = ifft(Y_noisy)  
y_reconstructed = np.real(y_reconstructed)
t = t[range(n//2)]
plt.plot(t, y_reconstructed, 'k')
plt.title('Reconstructed signal')
plt.show()
```

Plot the reconstructed signal.Plot the original signal and the reconstructed signal on two separate subplots for comparison.
```python
y = y[range(n//2)]
plt.subplot(2,1,1)
plt.plot(t, y, 'k')
plt.title('Original signal')

plt.subplot(2,1,2)
plt.plot(t, y_reconstructed, 'k')
plt.title('Reconstructed signal')
plt.show()
```
