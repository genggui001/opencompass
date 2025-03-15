---
jupyter:
  title: Signal Processing and Fourier Transformation of a Sinusoidal Signal
  module: SciPy
  dataset: None
  difficulty: NORMAL
  idx: 9
  num_steps: 7
  step_types:
    - vis
    - vis
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - numpy & matplotlib
    - numpy & scipy & matplotlib
    - scipy & matplotlib
    - scipy & matplotlib
    - scipy & matplotlib
    - scipy & matplotlib
    - scipy & matplotlib
---

Generate a sinusoidal signal with a length of 500 and a range of 0 to 1. This signal is a combination of two sine waves, one with a frequency of 50 Hz and the other with a frequency of 80 Hz. Plot this signal using matplotlib to visualize it.
```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1.0, 500)
signal = np.sin(2*np.pi*50.0*t) + 0.5*np.sin(2*np.pi*80.0*t)
plt.figure()
plt.plot(t, signal)
plt.title('Original Signal')
plt.show()
```

Perform a Fourier transform on the signal to convert it from the time domain to the frequency domain. Plot the frequency-domain representation of the signal.
```python
from scipy.fftpack import fft

yf = fft(signal)
xf = np.linspace(0.0, 1.0/(2.0*(t[1]-t[0])), len(t)//2)
plt.plot(xf, 2.0/len(t) * np.abs(yf[0:len(t)//2]))
plt.title('Frequency Domain Signal')
plt.show()
```

Construct a lowpass Butterworth filter with an order of 5 and a cutoff frequency normalized to the Nyquist frequency. The Nyquist frequency is half the sample rate. Use the Butterworth filter to filter out high-frequency noise from the signal. The filter is applied using a forward and reverse digital IIR filter. Filter the signal using the lowpass filter with a cutoff frequency of 60 Hz. Plot the filtered signal.
```python
from scipy.signal import butter
from scipy.signal import lfilter

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

order = 6
fs = 500.0       
cutoff = 60.0    
y = butter_lowpass_filter(signal, cutoff, fs, order)
plt.plot(t, y)
plt.title('Filtered Signal')
plt.show()
```

Perform a convolution on the original signal and the filtered signal. Plot the convolved signal.
```python
from scipy.signal import convolve

convolved = convolve(signal, y)
plt.plot(convolved)
plt.title('Convolved Signal')
plt.show()
```

Calculate the auto-correlation of the signal. Plot the correlated signal.
```python
from scipy.signal import correlate

correlated = correlate(signal, signal)
plt.plot(correlated)
plt.title('Correlated Signal')
plt.show()
```

Visualize the spectrogram of the signal. The frequencies should be in Hz and the time should be in seconds.
```python
from scipy.signal import spectrogram

frequencies, times, Sxx = spectrogram(signal, fs)
plt.pcolormesh(times, frequencies, 10*np.log10(Sxx))
plt.colorbar(label='Intensity [dB]')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.title('Spectrogram of the signal')
plt.show()
```

Perform a decimation on the signal by a factor of 4. Plot the decimated signal.
```python
from scipy.signal import decimate

decimated_signal = decimate(signal, 4)
plt.plot(decimated_signal)
plt.title('Decimated Signal')
plt.show()
```