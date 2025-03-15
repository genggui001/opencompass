---
jupyter:
  title:  Analyzing and Visualizing an Audio Signal.
  module: matplotlib
  dataset: none
  difficulty: DIFFICULT
  idx: 49
  num_steps: 6
  step_types:
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - matplotlib & scipy
    - matplotlib & numpy
    - matplotlib
    - matplotlib
    - matplotlib
---

File Path: "data/matplotlib_dataset49_sine.wav".

Use the read function from scipy's wavfile module to load the audio data from the file 'sine.wav'. This will return the sample rate of the audio and the audio signal itself.
Visualize the audio signal.
Plot the first 500 samples of the audio data using matplotlib's plot function. Label the x-axis as 'Sample' and y-axis as 'Amplitude'. Give the plot a title of 'Audio Signal'.
```python
from scipy.io import wavfile
sample_rate, signal = wavfile.read('./data/matplotlib_dataset49_sine.wav')
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 4))
plt.plot(signal[:500])
plt.title('Audio Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.show()
```

Compute the Fourier Transform of the audio signal. Then, compute the absolute value of the Fourier Transform to get the magnitude of the signal.
Plot the power spectral density.
Create a frequency array that ranges from 0 to the sample rate. Then, plot the first half of the magnitude array against the first half of the frequency array. Label the x-axis as 'Frequency' and y-axis as 'Magnitude'. Give the plot a title of 'Power Spectral Density'.
```python
import numpy as np
fft = np.fft.fft(signal)
magnitude = np.abs(fft)
f = np.linspace(0, sample_rate, len(magnitude))
plt.figure(figsize=(10, 4))
plt.plot(f[:int(len(magnitude)/2)], magnitude[:int(len(magnitude)/2)])
plt.title('Power Spectral Density')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.show()
```

Use matplotlib's specgram function to generate a spectrogram of the audio signal amplitude with a window size of 1024 and overlap of 900.
```python
plt.specgram(signal[:, 1], NFFT=1024, Fs=2, noverlap=900)
plt.show()
```

Use the 'hot' color map to make the spectrogram more visually appealing.
Increase the window size to 2048 and overlap to 1900 to get a more detailed spectrogram.
```python
plt.specgram(signal[:, 1], NFFT=2048, Fs=2, noverlap=1900, cmap='hot')
plt.show()
```

Set the color limits of the spectrogram to -80 and 0 to highlight the most important parts.
```python
plt.specgram(signal[:, 1], NFFT=2048, Fs=2, noverlap=1900, cmap='hot', clim=(-80, 0))
plt.colorbar()
plt.show()
```
