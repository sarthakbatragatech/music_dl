import os
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

sound_path = 'data/sample/not_smart.wav'
sample_rate, samples = wavfile.read(sound_path)
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

plt.pcolormesh(times, frequencies, spectrogram)
plt.imshow(spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig(sound_path[:-4] + '.png', transparent = False)
plt.show()
