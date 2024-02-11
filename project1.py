import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import librosa
import soundfile as sf
import sounddevice as sd

# Config
# Record mode setting
#   if == 1, prompt user for rec_fname, record and save to file
#   if == 0, prompt user for rec_fname to analyze
record_mode = 1
duration = 5
fs = 48000
sd.default.device = 0

def record(rec_fname):
    # Record sample from laptop mic
    print("RECORDING")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()  # Wait until finished recording
    print("Done recording")
    
    # Plot in time domain
    # Change xaxis unit from samples to seconds
    time_seconds = np.arange(len(recording)) / fs
    plt.plot(time_seconds, recording)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.title('Audio waveform - '+rec_fname)
    plt.savefig(rec_fname+"-TD.png")
    plt.show()
    
    # Write audio to file
    sf.write(rec_fname+".wav", recording, fs)

if record_mode == 1:
    rec_fname = input("Enter filename for recording (omit extension):")
    record(rec_fname)
else:
    rec_fname = input("Enter filename to analyze (omit extension):")

# Open file using librosa
audio, sr = librosa.load(rec_fname+".wav",sr=fs)
print(audio.shape)

freq = librosa.amplitude_to_db(np.abs(librosa.stft(audio)), ref=np.max)
print(freq.shape)

# Create and format spectrogram
librosa.display.specshow(freq,sr=sr, x_axis='time', y_axis='linear')
plt.ylim([0,8000])
plt.title('Spectrogram - '+rec_fname)
plt.savefig(rec_fname+"-SG.png")
plt.show()