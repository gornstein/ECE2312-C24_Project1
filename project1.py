import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import librosa
import soundfile as sf
import sounddevice as sd

# Config
duration = 3
fs = 48000
sd.default.device = 0

# Record sample from laptop mic
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
sd.wait()  # Wait until finished recording
# sd.play(recording,fs)

plt.plot(recording)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Audio in time domain')
plt.show()

# Write audio to file
sf.write('recorded_audio.wav', recording, fs)

# Open file using librosa
audio, sr = librosa.load('recorded_audio.wav',sr=fs)
print(audio.shape)

freq = librosa.amplitude_to_db(np.abs(librosa.stft(audio)), ref=np.max)
print(freq.shape)

# Create and format spectrograph
librosa.display.specshow(freq,sr=sr, x_axis='time', y_axis='linear')
plt.title('Spectrograph')
plt.show()